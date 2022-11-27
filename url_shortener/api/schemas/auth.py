from .base import Base
from pydantic import validator
from url_shortener.config import get_settings


class Token(Base):
    token: str
    type: str = "bearer"


class RegistrationForm(Base):
    username: str
    password: str

    @validator("password")
    def validate_password(cls, password):
        settings = get_settings()
        password = settings.PWD_CONTEXT.hash(password)
        return password


class User(Base):
    db_id: str
    username: str
