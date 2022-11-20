from pydantic import AnyUrl
from .base import Base


class UrlPostRequest(Base):
    long_url: AnyUrl


class UrlPostResponse(Base):
    short_url: AnyUrl
