from url_shortener.db.repository import (
    PostgresRepositoryUrl,
    PostgresRepositoryAuth,
    FakeRepositoryAuth,
    FakeRepositoryUrl,
)
from url_shortener.db import PgSession
from .auth_service import AuthService, FakeAuthService, InterfaceAuthService
from .url_service import UrlService, FakeUrlService, InterfaceUrlService


class Config:
    fake: bool = False


def get_url_service() -> InterfaceUrlService:
    if Config.fake:
        return FakeUrlService([], FakeRepositoryUrl)
    return UrlService(PgSession.get_session(), PostgresRepositoryUrl)


def get_auth_service() -> InterfaceAuthService:
    if Config.fake:
        return FakeAuthService([], FakeRepositoryAuth)
    return AuthService(PgSession.get_session(), PostgresRepositoryAuth)
