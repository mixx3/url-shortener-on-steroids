from typing import Any
from uuid import UUID
from .base import BaseRepository


class FakeRepository(BaseRepository):
    container: set = set()

    def add(self, item: Any):
        self.container.add(item.id)

    def get(self, table: Any, id: UUID) -> bool:
        return id in self.container
