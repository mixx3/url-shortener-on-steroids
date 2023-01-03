from .settings import PgSettings, DefaultSettings
from typing import Type
from functools import lru_cache


@lru_cache()
def get_settings(
        settings: Type[DefaultSettings] = PgSettings
):
    settings = settings()
    return settings
