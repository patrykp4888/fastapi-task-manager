from pydantic import BaseSettings, field_validator, AnyHttpUrl, ConfigDict
from typing import List, Optional, Dict, Any
import secrets
import os


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "TaskFlow"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_uri(cls, v: Optional[str], info) -> str:
        if v:
            return v

        data = info.data
        return f"postgresql://{data.get('POSTGRES_USER')}:{data.get('POSTGRES_PASSWORD')}@{data.get('POSTGRES_SERVER')}/{data.get('POSTGRES_DB')}"

    @field_validator("SECRET_KEY", mode="before")
    @classmethod
    def set_secret_key(cls, v: Optional[str]) -> str:
        """Generates random SECRET_KEY if not given."""
        if v:
            return v
        return secrets.token_urlsafe(32)


settings = Settings()
