from typing import Type, Any
from .base import UrlBaseRepository, AuthBaseRepository
from sqlalchemy.orm import Session
from url_shortener.db.models import Base, Url, Auth
from uuid import UUID



class PostgresRepositoryUrl(UrlBaseRepository):
    def add(self, item: Url) -> None:
        self.session.add(item)
        self.session.flush()

    def get_by_id(self, id: UUID) -> Type[Base] | None:
        return self.session.query(Url).get(Url.id == id).one_or_none()

    def get_by_suffix(self, suffix: str) -> Url | None:
        return self.session.query(Url).filter(Url.suffix == suffix).one_or_none()

    def check_suffix_exists(self, suffix: str) -> bool:
        return self.get_by_suffix(suffix) is None


class PostgresRepositoryAuth(AuthBaseRepository):
    def add(self, item: Auth):
        self.session.add(item)
        self.session.flush()
