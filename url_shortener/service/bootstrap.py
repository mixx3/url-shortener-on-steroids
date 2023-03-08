from url_shortener.db.repository import (
    PostgresRepositoryUrl,
    PostgresRepositoryAuth,
    PostgresRepositoryLog,
    FakeRepositoryAuth,
    FakeRepositoryUrl,
    FakeRepositoryLog,
)
import url_shortener.db as PgSession
from .auth import AuthService, FakeAuthService, InterfaceAuthService
from .url import UrlService, FakeUrlService, InterfaceUrlService
from .log import LogService, InterfaceLogService, FakeLogService


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


async def get_log_service() -> InterfaceLogService:
    if Config.fake:
        return FakeLogService([], FakeRepositoryLog)
    return LogService(await PgSession.get_session(), PostgresRepositoryLog)
