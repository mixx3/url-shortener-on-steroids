from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID


class BaseRepository(ABC):
    @abstractmethod
    def add(self, item: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, table: Any, id: UUID) -> Any:
        raise NotImplementedError
