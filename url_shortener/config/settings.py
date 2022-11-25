from pydantic import BaseSettings, PostgresDsn, RedisDsn
from typing import Union
from passlib.context import CryptContext
from fastapi import Depends


class DefaultSettings(BaseSettings):
    DB_DSN: Union[PostgresDsn, RedisDsn, None] = None
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
    CORS_ALLOW_ORIGINS: list[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ["*"]
    CORS_ALLOW_HEADERS: list[str] = ["*"]

    class Config:
        """Pydantic BaseSettings config"""

        case_sensitive = True
        env_file = ".env"


class PgSettings(DefaultSettings):
    DB_DSN: PostgresDsn


class RedisSettings(DefaultSettings):
    DB_DSN: RedisDsn
