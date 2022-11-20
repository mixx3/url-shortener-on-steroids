from typing import Any
from uuid import UUID
from .base import BaseRepository


class RedisRepository(BaseRepository):
    def add(self, item: Any) -> None:
        pass

    def get(self, table: Any, id: UUID) -> dict:
        pass

