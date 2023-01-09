from pydantic import AnyUrl
from .base import Base


class UrlPostRequest(Base):
    long_url: AnyUrl


class UrlPostResponse(Base):
    long_url: AnyUrl
    short_url: AnyUrl | None
    suffix: str | None
