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

    @abstractmethod
    def get_by_suffix(self, suffix: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    def check_suffix_exists(self, suffix: str) -> bool:
        raise NotImplementedError
