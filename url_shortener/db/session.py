import abc
import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from url_shortener.config import get_settings


class DbSession(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def get_session(cls):
        raise NotImplementedError


class PgSession(DbSession):
    @classmethod
    def get_session(cls) -> sqlalchemy.orm.Session:
        engine = create_engine(get_settings().DB_DSN)
        session = sessionmaker(engine, autocommit=True)
        with session() as s:
            return s
