from .base import BaseService
from abc import abstractmethod
from pydantic import AnyUrl
from random import choice
from string import ascii_uppercase
from url_shortener.db import models
import requests
from .exceptions import InvalidUrl, ObjectNotFound


class InterfaceUrlService(BaseService):
    @abstractmethod
    async def make_suffix(self, url: AnyUrl) -> str:
        raise NotImplementedError

    @staticmethod
    async def _generate_suffix():
        raise NotImplementedError

    @abstractmethod
    async def get_long_url(self, suffix):
        raise NotImplementedError

    @staticmethod
    async def _ping_url(url: AnyUrl) -> bool:
        raise NotImplementedError


class UrlService(InterfaceUrlService):
    async def make_suffix(self, url: AnyUrl) -> str:
        is_valid = await self._ping_url(url)
        if is_valid:
            suffix = await self._generate_suffix()
            db_url = models.Url(origin_url=url, suffix=suffix)
            self.repository.add(db_url)
            return suffix
        raise InvalidUrl(url)

    async def _generate_suffix(self):
        while True:
            suffix = "".join(choice(ascii_uppercase) for _ in range(6))
            if self.repository.check_suffix_exists(suffix):
                return suffix

    async def get_long_url(self, suffix):
        url = self.repository.get_by_suffix(suffix)
        if url is None:
            return ObjectNotFound(suffix)
        return url.to_dict()

    @staticmethod
    async def _ping_url(url: AnyUrl) -> bool:
        try:
            res = requests.get(url)
            return res.status_code < 400
        except requests.exceptions.ConnectionError:
            return False


class FakeUrlService(InterfaceUrlService):
    async def make_suffix(self, url: AnyUrl) -> str:
        is_valid = await self._ping_url(url)
        if is_valid:
            suff = await self._generate_suffix()
            self.repository.add(models.Url(origin_url=url, suffix=suff))
            return suff
        raise InvalidUrl(url)

    @staticmethod
    async def _generate_suffix():
        return "".join(choice(ascii_uppercase) for _ in range(6))

    async def get_long_url(self, suffix):
        for u in self.repository:
            if u.suffix == suffix:
                return u.origin_url

    @staticmethod
    async def _ping_url(url: AnyUrl) -> bool:
        if url == "https://www.python.org":
            return True
        return False
