import cmath
import re

import sqlalchemy.dialects.postgresql
from datetime import datetime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from uuid import uuid4
from sqlalchemy import Column


@as_declarative()
class Base:
    """Base class for all database entities"""

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:  # pylint: disable=no-self-argument
        """Generate database table name automatically.
        Convert CamelCase class name to snake_case db table name.
        """
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()

    def __repr__(self) -> str:
        attrs = []
        for c in self.__table__.columns:
            attrs.append(f"{c.name}={getattr(self, c.name)}")
        return "{}({})".format(self.__class__.__name__, ', '.join(attrs))

    def to_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Url(Base):
    id = Column(
        sqlalchemy.dialects.postgresql.UUID(as_uuid=True),
        primary_key=True,
        server_default=uuid4(),
        unique=True,
        doc="URL id",
    )
    origin_url = Column(
        sqlalchemy.String,
        nullable=False,
        index=True,
        doc="Original long url",
    )
    suffix = Column(
        sqlalchemy.String,
        nullable=False,
        index=True,
        doc="Short url suffix",
    )
    create_ts = Column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow(),
        doc="DateTime when created",
    )
