from .base import BaseService
from url_shortener.db.models import Auth
import url_shortener.service.exceptions as exc
from url_shortener.config import get_settings
import jwt
from datetime import datetime

settings = get_settings()


class AuthService(BaseService):
    async def registrate_user(self, username, password):
        db_user = self.repository.get_user_by_username(username)
        if db_user:
            raise exc.AlreadyRegistered(username)
        else:
            self.repository.add(Auth(username=username, password=password))

    async def authenticate_user(self, username, password) -> Auth | None:
        db_user: Auth | None = self.repository.get_user_by_username(username)
        if not db_user:
            raise exc.NotRegistered(username)
        if not self._validate_password(db_user.password, password):
            raise exc.WrongPassword()
        return db_user

    @staticmethod
    async def _validate_password(db_password, inp_password):
        return db_password == inp_password

    @staticmethod
    async def create_token(**kwargs):
        payload = kwargs.copy()
        expire_date = datetime.utcnow() + settings.EXPIRY_TIMEDELTA
        payload.update({"expire": expire_date.isoformat()})
        token = jwt.encode(payload=payload, key=settings.JWT_KEY)
        return token

    async def get_me(self, token) -> Auth | None:
        try:
            user = jwt.decode(token, settings.JWT_KEY)
        except jwt.DecodeError:
            raise exc.WrongToken()
        return self.repository.get_user_by_username(user['username'])
