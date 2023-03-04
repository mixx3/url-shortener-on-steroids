from url_shortener.db.repository import (
    PostgresRepositoryUrl,
    PostgresRepositoryAuth,
    FakeRepositoryAuth,
    FakeRepositoryUrl,
)
import url_shortener.db as PgSession
from .auth_service import AuthService, FakeAuthService, InterfaceAuthService
from .url_service import UrlService, FakeUrlService, InterfaceUrlService


class Config:
    fake: bool = False


async def get_url_service() -> InterfaceUrlService:
    if Config.fake:
        return FakeUrlService([], FakeRepositoryUrl)
    return UrlService(await PgSession.get_session(), PostgresRepositoryUrl)


async def get_auth_service() -> InterfaceAuthService:
    if Config.fake:
        return FakeAuthService([], FakeRepositoryAuth)
    return AuthService(await PgSession.get_session(), PostgresRepositoryAuth)
