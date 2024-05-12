from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.api.deps import get_db
from app.models.kidbright import Kidbright
from app.schemas.soil import SoilBase

router = APIRouter(prefix="/soil", tags=["Soil"])


@router.get(
    "/current", response_model=SoilBase, summary="Returns current hour soil details"
)
def get_current_soil(db: Session = Depends(get_db)):
    current_soil = db.query(Kidbright).order_by(Kidbright.id.desc()).first()

    if not current_soil:
        raise HTTPException(status_code=404, detail="Soil data not found")

    return current_soil


@router.get(
    "/hour/{specific_date}/{hour}",
    response_model=SoilBase,
    summary="Returns soil details for a specified date and hour",
)
def get_soil_by_hour(specific_date: date, hour: int, db: Session = Depends(get_db)):
    soil_data = (
        db.query(Kidbright)
        .filter(
            func.date(Kidbright.ts) == specific_date,
            func.extract("hour", Kidbright.ts) == hour,
        )
        .order_by(Kidbright.ts.asc())
        .first()
    )

    if not soil_data:
        raise HTTPException(
            status_code=404,
            detail="Soil data not found for the specified date and hour",
        )

    return soil_data
