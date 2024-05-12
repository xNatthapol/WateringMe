from sqlalchemy import Column, DateTime, Float, Integer

from app.db.session import Base


class PET(Base):
    __tablename__ = "frc_pet"

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime)
    lat = Column(Float)
    lon = Column(Float)
    pet = Column(Float)
