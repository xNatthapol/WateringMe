from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

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

# CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# Include routes
app.include_router(api_router)


@app.get("/", include_in_schema=False)
async def redirect_docs():
    return RedirectResponse(settings.DOCS_URL)
