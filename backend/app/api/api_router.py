from fastapi import APIRouter

from .routes import weather

api_router = APIRouter()

api_router.include_router(weather.router)
