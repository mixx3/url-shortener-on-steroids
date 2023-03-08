from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(ABC):
    def __init__(self, session):
        self.session : AsyncSession | None = session

    @abstractmethod
    async def add(self, item: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Any:
        raise NotImplementedError


class UrlBaseRepository(BaseRepository):
    @abstractmethod
    async def get_by_suffix(self, suffix: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def check_suffix_exists(self, suffix: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> Any:
        raise NotImplementedError


class AuthBaseRepository(BaseRepository):
    @abstractmethod
    async def get_user_by_username(self, username):
        raise NotImplementedError

    @abstractmethod
    async def validate_password(self, password):
        raise NotImplementedError


class LogBaseRepository(BaseRepository):
    @abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_by_url_id(self, url_id: UUID) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def add(self, item: dict) -> None:
        raise NotImplementedError
    

class FakeRepository(BaseRepository):
    container = []

    def add(self, obj):
        self.container.append(obj)

    def get_by_id(self, id: UUID) -> Any:
        for o in self.container:
            if o.id == id:
                return o
