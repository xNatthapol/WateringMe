from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(BASE_DIR / ".env"))

    TITLE: str
    DESCRIPTION: str

    ROOT_PATH: str
    DOCS_URL: str
    REDOC_URL: str

    DATABASE_URL: str


settings = Settings()
