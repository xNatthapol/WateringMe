from datetime import datetime

from pydantic import BaseModel


class WateringBase(BaseModel):
    ts: datetime
    lat: float
    lon: float
    condi: str
    temper: float
    humid: float
    sm: float
    suggest: str
