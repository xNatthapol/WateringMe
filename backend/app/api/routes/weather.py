from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.api.deps import get_db
from app.models.kidbright import Kidbright
from app.models.weather import Weather
from app.schemas.weather import WeatherBase

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get("/current", response_model=WeatherBase)
def get_current_weather(db: Session = Depends(get_db)):
    current_weather = (
        db.query(
            Weather.ts,
            Weather.lat,
            Weather.lon,
            Weather.condi,
            Weather.conic,
            Weather.humid,
            Weather.temper,
            Weather.precip,
            Kidbright.light,
        )
        .join(
            Kidbright,
            (func.date(Weather.ts) == func.date(Kidbright.ts))
            & (func.extract("hour", Weather.ts) == func.extract("hour", Kidbright.ts)),
        )
        .order_by(Weather.id.desc())
        .first()
    )

    if not current_weather:
        raise HTTPException(status_code=404, detail="Weather data not found")

    return current_weather
