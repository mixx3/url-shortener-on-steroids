from .base import BaseService
from pydantic import AnyUrl
from random import choice
from string import ascii_uppercase
from url_shortener.db import models
import requests
from .exceptions import InvalidUrl, ObjectNotFound


class AdminService(BaseService):
    pass


class UrlService(BaseService):
    async def make_suffix(self, url: AnyUrl) -> str:
        is_valid = await self._ping_url(url)
        if is_valid:
            suffix = await self._generate_suffix()
            db_url = models.Url(origin_url=url, suffix=suffix)
            self.repository.add(db_url)
            return suffix
        else:
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

    @staticmethod
    async def _ping_url(url: AnyUrl) -> bool:
        res = requests.get(url)
        return res.status_code < 400
