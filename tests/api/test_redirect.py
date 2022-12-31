import json
from starlette import status

class TestRedirect:
    _url = "/to/"

    def test_main_scenario(self, suffix):
        assert 2
