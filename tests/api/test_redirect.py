import json
from starlette import status


class TestRedirect:
    _url = "/to/"

    def test_main_scenario(self, client, suffix_body):
        res = client.get(f"{self._url}{suffix_body['suffix']}")
        assert res.url == "https://www.python.org"
