from typing import Any

from .base import UrlBaseRepository, AuthBaseRepository, LogBaseRepository
from url_shortener.db.models import Url, Auth, UrlLog
from uuid import UUID
import sqlalchemy as sa


class PostgresRepositoryUrl(UrlBaseRepository):
    async def add(self, item: dict) -> None:
        q = sa.insert(Url).values(**item).returning(Url)
        await self.session.scalar(q)
        await self.session.flush()

    async def get_by_id(self, id: UUID) -> Url | None:
        q = sa.select(Url).where(Url.id == id)
        return await self.session.scalar(q)

    async def get_by_suffix(self, suffix: str) -> Url | None:
        q = sa.select(Url).where(Url.suffix == suffix)
        return await self.session.scalar(q)

    async def check_suffix_exists(self, suffix: str) -> bool:
        return await self.get_by_suffix(suffix) is None

    async def get_by_user_id(self, user_id: UUID) -> list[Url]:
        q = sa.select(Url).where(Url.user_id == user_id)
        return await self.session.scalar(q)


class PostgresRepositoryAuth(AuthBaseRepository):
    async def add(self, item: dict):
        q = sa.insert(Auth).values(**item).returning(Auth)
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


class PostgresRepositoryLog(LogBaseRepository):
    async def get_by_user_id(self, user_id: UUID) -> Any:
        q = sa.select(UrlLog).where(UrlLog.user_id == user_id)
        return await self.session.scalars(q)

    async def get_by_url_id(self, url_id: UUID) -> Any:
        q = sa.select(UrlLog).where(UrlLog.url_id == url_id)
        return await self.session.scalars(q)

    async def add(self, item: dict) -> None:
        q = sa.insert(UrlLog).values(**dict).returning(UrlLog)
        await self.session.execute(q)
        await self.session.flush()

    async def get_by_id(self, id: UUID) -> Any:
        return await self.session.scalar(sa.select(UrlLog).where(UrlLog.id == id))