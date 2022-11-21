from url_shortener.service.url_service import UrlService
from url_shortener.db.repository import PostgresRepositoryUrl
from url_shortener.db import PgSession
from url_shortener.service.auth_service import AuthService
from url_shortener.db.repository import PostgresRepositoryAuth


def pg_url_service():
    return UrlService(PgSession.get_session(), PostgresRepositoryUrl)


def pg_auth_service():
    return AuthService(PgSession.get_session(), PostgresRepositoryAuth)
