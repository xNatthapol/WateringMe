from fastapi import APIRouter

from .routes import soil, weather, pet, watering

api_router = APIRouter()

api_router.include_router(soil.router)
api_router.include_router(weather.router)
api_router.include_router(pet.router)
api_router.include_router(watering.router)
