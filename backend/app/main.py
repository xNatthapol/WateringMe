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
    allow_origins=["http://localhost", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Include routes
app.include_router(api_router)


@app.get("/")
async def redirect_docs():
    return RedirectResponse(settings.DOCS_URL)
