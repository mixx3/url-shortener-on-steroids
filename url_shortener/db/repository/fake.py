from typing import Any
from uuid import UUID
from .base import UrlBaseRepository, AuthBaseRepository


class FakeRepositoryUrl(UrlBaseRepository):
    def get_by_user_id(self, user_id: UUID) -> Any:
        pass

    container: list = []

    def add(self, item: Any):
        self.container.append(item)

    def get_by_suffix(self, suffix: str) -> Any:
        for i in self.container:
            if i.suffix == suffix:
                return i

    def get_by_id(self, id: UUID) -> Any:
        pass

    def check_suffix_exists(self, suffix: str) -> bool:
        return suffix in self.container


class FakeRepositoryAuth(AuthBaseRepository):
    container: set[str] = set()

    def add(self, item: Any) -> None:
        pass

    def validate_password(self, password):
        pass

    def get_by_id(self, id: UUID) -> Any:
        pass

    def get_user_by_username(self, username):
        pass
