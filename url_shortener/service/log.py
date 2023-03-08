from .base import BaseService
from abc import abstractmethod

class InterfaceLogService(BaseService):
    @abstractmethod
    async def get_logs_for_user(self, user_id):
        raise NotImplementedError

    @abstractmethod
    async def get_logs_for_url(self, url_id):
        raise NotImplementedError

    @abstractmethod
    async def add_log(self, item):
        raise NotImplementedError


class LogService(InterfaceLogService):
    async def get_logs_for_user(self, user_id):
        return await self.repository.get_by_user_id(user_id)

    async def get_logs_for_url(self, url_id):
        return await self.repository.get_by_url_id(url_id)

    async def add_log(self, item):
        return await self.repository.add(item)


class FakeLogService(InterfaceLogService):
    async def get_logs_for_user(self, user_id):
        pass

    async def get_logs_for_url(self, url_id):
        pass

    async def add_log(self, item):
        pass
