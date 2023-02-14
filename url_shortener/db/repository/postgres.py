from .base import UrlBaseRepository, AuthBaseRepository
from url_shortener.db.models import Url, Auth
from uuid import UUID
import sqlalchemy as sa


class PostgresRepositoryUrl(UrlBaseRepository):
    def add(self, item: Url) -> None:
        q = sa.insert(Url).values(**item.to_dict()).returning(Url)
        self.session.scalar(q)
        self.session.flush()

    def get_by_id(self, id: UUID) -> Url | None:
        q = sa.select(Url).where(Url.id == id)
        return self.session.scalar(q)

    def get_by_suffix(self, suffix: str) -> Url | None:
        q = sa.select(Url).where(Url.suffix == suffix)
        return self.session.scalar(q)

    def check_suffix_exists(self, suffix: str) -> bool:
        return self.get_by_suffix(suffix) is None

    def get_by_user_id(self, user_id: UUID) -> list[Url]:
        q = sa.select(Url).where(Url.user_id == user_id)
        return self.session.scalar(q)


class PostgresRepositoryAuth(AuthBaseRepository):
    def add(self, item: Auth):
        q = sa.insert(Auth).values(**item.to_dict()).returning(Auth)
        self.session.scalar(q)
        self.session.flush()

    def get_by_id(self, id: UUID) -> Auth:
        q = sa.select(Auth).where(Auth.id == id)
        return self.session.scalar(q)

    def get_user_by_username(self, username) -> Auth:
        q = sa.select(Auth).where(Auth.username == username)
        return self.session.scalar(q)

    def validate_password(self, password):
        q = sa.select(Auth).where(Auth.password == password)
        return self.session.scalar(q) is not None
