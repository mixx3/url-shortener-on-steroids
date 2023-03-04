from .base import BaseService
from url_shortener.db.models import Auth
import url_shortener.service.exceptions as exc
from url_shortener.config import get_settings
from abc import abstractmethod

settings = get_settings()


class InterfaceAuthService(BaseService):
    @abstractmethod
    async def registrate_user(self, username, password):
        raise NotImplementedError

    @abstractmethod
    async def authenticate_user(self, username, password) -> Auth | None:
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, username):
        raise NotImplementedError

    @staticmethod
    async def _validate_password(db_password, inp_password):
        raise NotImplementedError


class AuthService(InterfaceAuthService):
    async def registrate_user(self, username, password):
        db_user = self.repository.get_user_by_username(username)
        if db_user:
            raise exc.AlreadyRegistered(username)
        else:
            await self.repository.add(Auth(username=username, password=password))

    async def authenticate_user(self, username, password) -> Auth | None:
        db_user: Auth | None = await self.repository.get_user_by_username(username)
        if not db_user:
            raise exc.NotRegistered(username)
        if not await self._validate_password(db_user.password, password):
            raise exc.WrongPassword()
        return db_user

    async def get_user(self, username):
        return await self.repository.get_user_by_username(username)

    @staticmethod
    async def _validate_password(db_password, inp_password):
        return settings.PWD_CONTEXT.verify(inp_password, db_password)


class FakeAuthService(InterfaceAuthService):
    repository = []

    async def registrate_user(self, username, password):
        self.repository.append(Auth(id="fake", username=username, password=password))

    async def authenticate_user(self, username, password) -> Auth | None:
        for auth in self.repository:
            if auth.password == password and auth.username == username:
                return auth
        raise exc.NotRegistered(username)

    async def get_user(self, username):
        for auth in self.repository:
            if auth.username == username:
                return auth
        raise exc.NotRegistered(username)

    @staticmethod
    async def _validate_password(db_password, inp_password):
        return settings.PWD_CONTEXT.verify(inp_password, db_password)
