from datetime import date, datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.api.deps import get_db
from app.models.kidbright import Kidbright
from app.models.weather import Weather, WeatherForecast
from app.schemas.weather import WeatherBase, WeatherForecastBase

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get(
    "/current",
    response_model=WeatherBase,
    summary="Returns currently hour weather details",
)
def get_current_weather(db: Session = Depends(get_db)):
    current_weather = (
        db.query(
            Weather.ts,
            Weather.lat,
            Weather.lon,
            Weather.condi,
            Weather.conic,
            Weather.humid,
            Weather.temper,
            Weather.precip,
            Kidbright.light,
        )
        .join(
            Kidbright,
            (func.date(Weather.ts) == func.date(Kidbright.ts))
            & (func.extract("hour", Weather.ts) == func.extract("hour", Kidbright.ts)),
        )
        .order_by(Weather.id.desc())
        .first()
    )

    if not current_weather:
        raise HTTPException(status_code=404, detail="Weather data not found")

    return current_weather


@router.get(
    "/forecast",
    response_model=List[WeatherForecastBase],
    summary="Returns a list of forecast weather details at the current day",
)
def get_forecast_weather(db: Session = Depends(get_db)):
    # Get the start and end of the current day
    today_start = datetime.combine(date.today(), datetime.min.time())
    today_end = datetime.combine(date.today(), datetime.max.time())

    forecast_weather = (
        db.query(WeatherForecast)
        .filter(WeatherForecast.ts >= today_start, WeatherForecast.ts <= today_end)
        .order_by(WeatherForecast.ts.asc())
        .all()
    )

    if not forecast_weather:
        raise HTTPException(status_code=404, detail="Weather forecast data not found")

    return forecast_weather


@router.get(
    "/hour/{date}/{hour}",
    response_model=WeatherBase,
    summary="Returns weather details at specified date and hour",
)
def get_weather_by_hour(date: date, hour: int, db: Session = Depends(get_db)):
    weather_data = (
        db.query(
            Weather.ts,
            Weather.lat,
            Weather.lon,
            Weather.condi,
            Weather.conic,
            Weather.humid,
            Weather.temper,
            Weather.precip,
            Kidbright.light,
        )
        .join(
            Kidbright,
            (func.date(Weather.ts) == func.date(Kidbright.ts))
            & (func.extract("hour", Weather.ts) == func.extract("hour", Kidbright.ts)),
        )
        .filter(
            func.date(Weather.ts) == date,
            func.extract("hour", Weather.ts) == hour,
        )
        .order_by(Weather.ts.asc())
        .first()
    )

    if not weather_data:
        raise HTTPException(
            status_code=404,
            detail="Weather data not found for the specified date and hour",
        )

    return weather_data


@router.get(
    "/hour/{date}",
    response_model=List[WeatherBase],
    summary="Returns weather details at the specific date",
)
def get_weather_by_date(date: date, db: Session = Depends(get_db)):
    weather_data = (
        db.query(
            Weather.ts,
            Weather.lat,
            Weather.lon,
            Weather.condi,
            Weather.conic,
            Weather.humid,
            Weather.temper,
            Weather.precip,
            Kidbright.light,
        )
        .join(
            Kidbright,
            (func.date(Weather.ts) == func.date(Kidbright.ts))
            & (func.extract("hour", Weather.ts) == func.extract("hour", Kidbright.ts)),
        )
        .filter(func.date(Weather.ts) == date)
        .order_by(Weather.ts.asc())
        .all()
    )

    if not weather_data:
        raise HTTPException(
            status_code=404,
            detail="Weather data not found at the specified date",
        )

    return weather_data
