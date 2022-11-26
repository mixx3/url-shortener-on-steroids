from .base import BaseService
from url_shortener.db.models import Auth
import url_shortener.service.exceptions as exc


class AuthService(BaseService):
    async def registrate_user(self, username, password):
        db_user = self.repository.get_user_by_username(username)
        if db_user:
            raise exc.AlreadyRegistered(username)
        else:
            self.repository.add(Auth(username=username, password=password))

    async def authenticate_user(self, username, password):
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
    async def create_token(self):
        pass
