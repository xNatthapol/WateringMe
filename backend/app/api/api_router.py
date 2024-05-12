from fastapi import APIRouter

from .routes import pet, soil, watering, weather

api_router = APIRouter()

api_router.include_router(watering.router)
api_router.include_router(soil.router)
api_router.include_router(weather.router)
api_router.include_router(pet.router)
