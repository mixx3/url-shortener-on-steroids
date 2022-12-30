from .settings import PgSettings, DefaultSettings, RedisSettings
from typing import Type
from functools import lru_cache
from url_shortener.service import InterfaceUrlService, InterfaceAuthService, pg_url_service, pg_auth_service


@lru_cache()
def get_settings(
        settings: Type[DefaultSettings] = PgSettings,
        auth_service: InterfaceAuthService = pg_auth_service(),
        url_service: InterfaceUrlService = pg_url_service(),
):
    settings = settings()
    settings.AUTH_SERVICE = auth_service
    settings.URL_SERVICE = url_service
    return settings
