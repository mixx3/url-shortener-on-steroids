from typing import Type
from .base import BaseRepository
from sqlalchemy.orm import Session
from url_shortener.db.models import Base
from uuid import UUID


class PostgresRepository(BaseRepository):
    def __init__(self, session: Session):
        self.session: Session = session

    def add(self, item: Type[Base]) -> None:
        self.session.add(item)
        self.session.flush()

    def get(self, table: Type[Base], id: UUID) -> Type[Base] | None:
        return self.session.query(table).get(id).one_or_none()

