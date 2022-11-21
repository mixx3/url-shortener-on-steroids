import abc
from url_shortener.db.repository import UrlBaseRepository
from typing import Type, Any


class BaseService(abc.ABC):
    def __init__(self, session: Any, repository: Type[UrlBaseRepository]):
        self.session = session
        self.repository = repository(session)
