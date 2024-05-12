from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.kidbright import Kidbright
from app.schemas.soil import SoilBase

router = APIRouter(prefix="/soil", tags=["Soil"])


@router.get("/current", response_model=SoilBase)
def get_current_soil(db: Session = Depends(get_db)):
    current_soil = db.query(Kidbright).order_by(Kidbright.id.desc()).first()

    if not current_soil:
        raise HTTPException(status_code=404, detail="Soil data not found")

    return current_soil
