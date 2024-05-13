from datetime import date, datetime, timedelta, timezone
from typing import List

import numpy as np
from fastapi import APIRouter, Depends, HTTPException
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.api.deps import get_db
from app.models.kidbright import Kidbright
from app.models.weather import Weather, WeatherForecast
from app.schemas.soil import SoilBase

router = APIRouter(prefix="/soil", tags=["Soil"])


@router.get(
    "/current", response_model=SoilBase, summary="Returns currently hour soil details"
)
async def get_current_soil(db: Session = Depends(get_db)):
    current_soil = db.query(Kidbright).order_by(Kidbright.id.desc()).first()

    if not current_soil:
        raise HTTPException(status_code=404, detail="Soil data not found")

    return current_soil


@router.get(
    "/forecast", response_model=List[SoilBase], summary="Return predicted soil details"
)
async def get_predicted_sm(db: Session = Depends(get_db)):

    historical_data = (
        db.query(Weather.temper, Weather.humid, Weather.precip, Kidbright.sm)
        .join(
            Kidbright,
            (func.date(Weather.ts) == func.date(Kidbright.ts))
            & (func.extract("hour", Weather.ts) == func.extract("hour", Kidbright.ts)),
        )
        .all()
    )

    current_date = (datetime.now(timezone.utc) + timedelta(hours=8)).date()
    current_hour = (datetime.now(timezone.utc) + timedelta(hours=7)).hour

    forecast_data = (
        db.query(
            WeatherForecast.ts,
            WeatherForecast.lat,
            WeatherForecast.lon,
            WeatherForecast.humid,
            WeatherForecast.temper,
            WeatherForecast.precip,
        )
        .filter(
            current_hour < func.extract("hour", WeatherForecast.ts),
            current_date == func.date(WeatherForecast.ts),
        )
        .all()
    )

    X = np.array([[data.temper, data.humid, data.precip] for data in historical_data])
    y = np.array([data.sm for data in historical_data])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()

    model.fit(X_train, y_train)

    predicted_sm_list = []
    for data in forecast_data:
        features = np.array([[data.temper, data.humid, data.precip]])
        predicted_sm = model.predict(features)
        predicted_sm_list.append(predicted_sm[0])

    soil_forecast_list = [
        SoilBase(ts=data.ts, lat=data.lat, lon=data.lon, sm=predicted_sm)
        for data, predicted_sm in zip(forecast_data, predicted_sm_list)
    ]

    return soil_forecast_list


@router.get(
    "/hour/{date}/{hour}",
    response_model=SoilBase,
    summary="Returns soil details at specified date and hour",
)
async def get_soil_by_hour(date: date, hour: int, db: Session = Depends(get_db)):

    if hour < 0:
        raise HTTPException(
            status_code=404,
            detail="Hour value cannot be negative",
        )

    soil_data = (
        db.query(Kidbright)
        .filter(
            func.date(Kidbright.ts) == date,
            func.extract("hour", Kidbright.ts) == hour,
        )
        .order_by(Kidbright.ts.asc())
        .first()
    )

    if not soil_data:
        raise HTTPException(
            status_code=404,
            detail="Soil data not found at specified date and hour",
        )

    return soil_data


@router.get(
    "/day/{date}",
    response_model=List[SoilBase],
    summary="Returns soil details at the specified date",
)
async def get_soil_by_date(date: date, db: Session = Depends(get_db)):
    soil_data = (
        db.query(Kidbright)
        .filter(
            func.date(Kidbright.ts) == date,
        )
        .order_by(Kidbright.ts.asc())
        .all()
    )

    if not soil_data:
        raise HTTPException(
            status_code=404,
            detail="Soil data not found for the specified date",
        )

    return soil_data
