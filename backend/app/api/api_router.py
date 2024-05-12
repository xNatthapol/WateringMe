from fastapi import APIRouter

from .routes import soil, weather

api_router = APIRouter()

api_router.include_router(soil.router)
api_router.include_router(weather.router)
