from datetime import datetime

from pydantic import BaseModel


class PETBase(BaseModel):
    ts: datetime
    lat: float
    lon: float
    pet: float
