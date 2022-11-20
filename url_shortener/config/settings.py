from pydantic import BaseSettings, PostgresDsn, RedisDsn
from typing import Union


class DefaultSettings(BaseSettings):
    DB_DSN: Union[PostgresDsn, RedisDsn, None] = None


class PgSettings(DefaultSettings):
    DB_DSN: PostgresDsn


class RedisSettings(DefaultSettings):
    DB_DSN: RedisDsn
