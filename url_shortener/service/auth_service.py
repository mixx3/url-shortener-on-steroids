from .base import BaseService
from url_shortener.db.models import Auth
from url_shortener.service.exceptions import AlreadyRegistered


class AuthService(BaseService):
    async def registrate_user(self, username, password):
        db_user = self.repository.get_user_by_username(username)
        if db_user:
            raise AlreadyRegistered(username)
        else:
            self.repository.add(Auth(username=username, password=password))
