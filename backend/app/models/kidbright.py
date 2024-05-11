from sqlalchemy import Column, DateTime, Float, Integer

from app.db.session import Base


class Kidbright(Base):
    __tablename__ = "kidbright"

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime)
    lat = Column(Float)
    lon = Column(Float)
    sm = Column(Float)
    light = Column(Float)
