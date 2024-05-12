from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(BASE_DIR / ".env"))

    # Project settings
    TITLE: str = "WateringMe"
    DESCRIPTION: str = "API of Project WateringMe"

    # PATH settings
    ROOT_PATH: str = "/"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"

    # Database settings
    DATABASE_URL: str

    # CORS settings
    CORS_ALLOW_ORIGINS: List[str] = ["*"]
    CORS_ALLOW_METHODS: List[str] = ["GET"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True


settings = Settings()
