from .base import UrlBaseRepository, AuthBaseRepository
from url_shortener.db.models import Url, Auth
from uuid import UUID
import sqlalchemy as sa


class PostgresRepositoryUrl(UrlBaseRepository):
    async def add(self, item: Url) -> None:
        q = sa.insert(Url).values(**item.to_dict()).returning(Url)
        self.session.scalar(q)
        self.session.flush()

    async def get_by_id(self, id: UUID) -> Url | None:
        q = sa.select(Url).where(Url.id == id)
        return self.session.scalar(q)

    async def get_by_suffix(self, suffix: str) -> Url | None:
        q = sa.select(Url).where(Url.suffix == suffix)
        return self.session.scalar(q)

    async def check_suffix_exists(self, suffix: str) -> bool:
        return self.get_by_suffix(suffix) is None

    async def get_by_user_id(self, user_id: UUID) -> list[Url]:
        q = sa.select(Url).where(Url.user_id == user_id)
        return self.session.scalar(q)


class PostgresRepositoryAuth(AuthBaseRepository):
    async def add(self, item: Auth):
        q = sa.insert(Auth).values(**item.to_dict()).returning(Auth)
        await self.session.execute(q)
        await self.session.flush()

    async def get_by_id(self, id: UUID) -> Auth:
        q = sa.select(Auth).where(Auth.id == id)
        return await self.session.scalar(q)

    async def get_user_by_username(self, username) -> Auth:
        q = sa.select(Auth).where(Auth.username == username)
        return await self.session.scalar(q)

    async def validate_password(self, password):
        q = sa.select(Auth).where(Auth.password == password)
        res = await self.session.scalar(q)
        return res is not None
