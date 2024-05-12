from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.api.deps import get_db
from app.models.pet import PET
from app.schemas.pet import PETBase

router = APIRouter(prefix="/pet", tags=["PET"])


@router.get(
    "/forecast",
    response_model=PETBase,
    summary="Returns PET at the current day",
)
def get_pet_per_day(db: Session = Depends(get_db)):
    forecast_pet = (
        db.query(PET.ts, PET.lat, PET.lon, PET.pet).order_by(PET.ts.desc()).first()
    )

    if not forecast_pet:
        raise HTTPException(status_code=404, detail="Weather data not found")

    return forecast_pet
