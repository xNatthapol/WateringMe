from fastapi import FastAPI

from app.api.api_router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    root_path=settings.ROOT_PATH,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    openapi_url=f"{settings.DOCS_URL}/openapi.json",
)

# include router
app.include_router(api_router)
