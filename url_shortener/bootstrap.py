from url_shortener.service.url_service import UrlService
from url_shortener.db.repository import PostgresRepository
from url_shortener.db import PgSession


def pg_url_service():
    return UrlService(PgSession.get_session(), PostgresRepository)
