from sqlalchemy import Column, DateTime, Float, Integer, Text

from app.db.session import Base


class Weather(Base):
    __tablename__ = "weather_api"

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime)
    lat = Column(Float)
    lon = Column(Float)
    condi = Column(Text)
    conic = Column(Text)
    humid = Column(Float)
    temper = Column(Float)
    precip = Column(Float)


class WeatherForecast(Base):
    __tablename__ = "weather_frc"

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime)
    lat = Column(Float)
    lon = Column(Float)
    condi = Column(Text)
    conic = Column(Text)
    humid = Column(Float)
    temper = Column(Float)
    precip = Column(Float)
    will_rain = Column(Integer)
    chance_rain = Column(Float)
