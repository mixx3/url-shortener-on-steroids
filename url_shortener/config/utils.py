from .settings import PgSettings, DefaultSettings, RedisSettings
from typing import Type
from functools import lru_cache


@lru_cache()
def get_settings(settings: Type[DefaultSettings] = PgSettings):
    return settings()
