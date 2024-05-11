from datetime import datetime

from pydantic import BaseModel


class WeatherBase(BaseModel):
    ts: datetime
    lat: float
    lon: float
    condi: str
    conic: str
    humid: float
    temper: float
    precip: float
    light: float
