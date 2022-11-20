import abc
from url_shortener.db.repository import BaseRepository
from typing import Type, Any


class BaseService(abc.ABC):
    def __init__(self, session: Any, repository: Type[BaseRepository]):
        self.session = session
        self.repository = repository(session)
