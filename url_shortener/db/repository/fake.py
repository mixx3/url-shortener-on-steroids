from typing import Any
from uuid import UUID
from .base import UrlBaseRepository


class FakeRepositoryUrl(UrlBaseRepository):
    container: set[str] = set()

    def add(self, item: Any):
        self.container.add(item)

    def get(self, table: Any, id: UUID) -> bool:
        return id in self.container

    def check_suffix_exists(self, suffix: str) -> bool:
        return suffix in self.container
