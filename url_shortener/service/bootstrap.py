from url_shortener.db.repository import (
    PostgresRepositoryUrl,
    PostgresRepositoryAuth,
    FakeRepositoryAuth,
    FakeRepositoryUrl,
)
from typing import Type
from url_shortener.db import PgSession
from .auth_service import AuthService, FakeAuthService
from .url_service import UrlService, FakeUrlService


def pg_url_service() -> UrlService:
    return UrlService(PgSession.get_session(), PostgresRepositoryUrl)


def pg_auth_service() -> AuthService:
    return AuthService(PgSession.get_session(), PostgresRepositoryAuth)


def fake_auth_service() -> FakeAuthService:
    return FakeAuthService(None, FakeRepositoryAuth)


def fake_url_service() -> FakeUrlService:
    return FakeUrlService(None, FakeRepositoryUrl)


class Config:
    fake: bool = False
    url_service: Type[UrlService] = pg_url_service
    auth_service: Type[AuthService] = pg_auth_service
    if fake:
        url_service: Type[FakeUrlService] = fake_url_service
        auth_service: Type[FakeAuthService] = fake_auth_service

