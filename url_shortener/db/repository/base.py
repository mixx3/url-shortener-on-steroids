from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID


class BaseRepository(ABC):
    def __init__(self, session):
        self.session = session

    @abstractmethod
    def add(self, item: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: UUID) -> Any:
        raise NotImplementedError


class UrlBaseRepository(BaseRepository):
    @abstractmethod
    def get_by_suffix(self, suffix: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    def check_suffix_exists(self, suffix: str) -> bool:
        raise NotImplementedError


class AuthBaseRepository(BaseRepository):
    @abstractmethod
    def get_user_by_username(self, username):
        raise NotImplementedError

    @abstractmethod
    def validate_password(self, password):
        raise NotImplementedError


class FakeRepository(BaseRepository):
    container = []

    def add(self, obj):
        self.container.append(obj)

    def get_by_id(self, id: UUID) -> Any:
        for o in self.container:
            if o.id == id:
                return o