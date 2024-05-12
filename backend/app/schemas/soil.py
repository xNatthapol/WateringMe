from datetime import datetime

from pydantic import BaseModel


class SoilBase(BaseModel):
    ts: datetime
    lat: float
    lon: float
    sm: float


class SoilForecastBase(SoilBase):
    pet: float
