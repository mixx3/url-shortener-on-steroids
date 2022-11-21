import abc
import sqlalchemy.orm
from url_shortener.config import get_settings, settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DbSession(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def get_session(cls):
        raise NotImplementedError


class PgSession(DbSession):
    @classmethod
    def get_session(cls) -> sqlalchemy.orm.Session:
        engine = create_engine(get_settings(settings.PgSettings).DB_DSN)
        session = sessionmaker(engine, autocommit=True)
        with session() as s:
            return s
