from pydantic import BaseSettings, PostgresDsn, RedisDsn
from typing import Union
from fastapi import Depends


class DefaultSettings(BaseSettings):
    DB_DSN: Union[PostgresDsn, RedisDsn, None] = None
    CORS_ALLOW_ORIGINS: list[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ['*']
    CORS_ALLOW_HEADERS: list[str] = ['*']


class PgSettings(DefaultSettings):
    DB_DSN: PostgresDsn


class RedisSettings(DefaultSettings):
    DB_DSN: RedisDsn
