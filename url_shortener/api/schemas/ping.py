from .base import Base
from pydantic import Field


class HealthResponse(Base):
    status: str = Field(default="OK!")
