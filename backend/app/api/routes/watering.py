from enum import Enum

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.api.deps import get_db
from app.models.kidbright import Kidbright
from app.models.weather import Weather
from app.schemas.watering import WateringBase

router = APIRouter(tags=["Watering suggestion"])


class SoilType(str, Enum):
    sandy = "Sandy"
    clay = "Clay"
    loam = "Loam"


@router.get(
    "/watering",
    response_model=WateringBase,
    summary="Returns weather details, current soil moisture level and suggestion",
)
async def get_condition(soil_type: SoilType, db: Session = Depends(get_db)):
    suggestion = ""
    weather_data = (
        db.query(
            Kidbright.ts,
            Kidbright.lat,
            Kidbright.lon,
            Weather.condi,
            Weather.temper,
            Weather.humid,
            Kidbright.sm,
        )
        .join(
            Kidbright,
            (func.date(Weather.ts) == func.date(Kidbright.ts))
            & (func.extract("hour", Weather.ts) == func.extract("hour", Kidbright.ts)),
        )
        .order_by(Weather.ts.desc())
        .first()
    )

    if soil_type == SoilType.sandy:
        suggestion = sandy_soil_suggestion(weather_data)
    elif soil_type == SoilType.clay:
        suggestion = clay_soil_suggestion(weather_data)
    elif soil_type == SoilType.loam:
        suggestion = loam_soil_suggestion(weather_data)

    return WateringBase(
        ts=weather_data.ts,
        lat=weather_data.lat,
        lon=weather_data.lon,
        condi=weather_data.condi,
        temper=weather_data.temper,
        humid=weather_data.humid,
        sm=weather_data.sm,
        suggest=suggestion,
    )


def sandy_soil_suggestion(weather_data):
    suggestion = ""
    if weather_data.sm < 80:
        suggestion = "Ensuring your plant's soil is moisturized"
        return suggestion

    if weather_data.condi in "rain" or weather_data.condi == "Mist":
        suggestion = "Reduce watering frequency to prevent waterlogging, as sandy soil drains quickly. Ensure proper drainage to avoid root rot."
    elif weather_data.temper > 30 and weather_data.humid > 70:
        suggestion = "Water deeply and less frequently to ensure moisture penetrates deeper into the sandy soil. Consider mulching to retain moisture."
    else:
        suggestion = (
            "Monitor soil moisture regularly and adjust watering frequency accordingly."
        )
    return suggestion


def clay_soil_suggestion(weather_data):
    suggestion = ""
    if weather_data.sm < 60:
        suggestion = "Ensuring your plant's soil is moisturized"
        return suggestion

    if weather_data.condi in "rain" or weather_data.condi == "Mist":
        suggestion = "Allow the soil to dry out slightly between watering to prevent waterlogging and promote healthy root growth. Avoid compacting the soil when wet."
    elif weather_data.temper > 30 > weather_data.humid:
        suggestion = "Water slowly and evenly to prevent runoff, as clay soil can become compacted when dry. Consider incorporating organic matter to improve water retention."
    else:
        suggestion = (
            "Monitor soil moisture regularly and adjust watering frequency accordingly."
        )
    return suggestion


def loam_soil_suggestion(weather_data):
    suggestion = ""
    if weather_data.sm < 70:
        suggestion = "Ensuring your plant's soil is moisturized"
        return suggestion

    if weather_data.condi in "rain" or weather_data.condi == "Mist":
        suggestion = "Water as needed, ensuring the soil remains consistently moist but not waterlogged. Monitor soil moisture regularly and adjust watering frequency accordingly."
    elif 20 <= weather_data.temper <= 25 and 40 <= weather_data.humid <= 60:
        suggestion = "Water as needed, ensuring the soil remains consistently moist but not waterlogged. Monitor soil moisture regularly and adjust watering frequency accordingly."
    else:
        suggestion = (
            "Monitor soil moisture regularly and adjust watering frequency accordingly."
        )
    return suggestion
