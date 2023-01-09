from .base import UrlBaseRepository, AuthBaseRepository
from url_shortener.db.models import Url, Auth
from uuid import UUID


class PostgresRepositoryUrl(UrlBaseRepository):
    def add(self, item: Url) -> None:
        self.session.add(item)
        self.session.flush()

    def get_by_id(self, id: UUID) -> Url | None:
        return self.session.query(Url).get(Url.id == id).one_or_none()

    def get_by_suffix(self, suffix: str) -> Url | None:
        return self.session.query(Url).filter(Url.suffix == suffix).one_or_none()

    def check_suffix_exists(self, suffix: str) -> bool:
        return self.get_by_suffix(suffix) is None

    def get_by_user_id(self, user_id: UUID) -> list[Url]:
        return self.session.query(Url).filter(Url.user_id == user_id).all()


class PostgresRepositoryAuth(AuthBaseRepository):
    def add(self, item: Auth):
        self.session.add(item)
        self.session.flush()

    def get_by_id(self, id: UUID) -> Auth:
        return self.session.query(Auth).filter(Auth.id == id).one_or_none()

    def get_user_by_username(self, username) -> Auth:
        return self.session.query(Auth).filter(Auth.username == username).one_or_none()

    def validate_password(self, password):
        return (
            self.session.query(Auth).filter(Auth.password == password).one_or_none()
            is not None
        )
