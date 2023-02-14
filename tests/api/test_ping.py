from starlette import status


class TestPing:
    _url = "/v1/health_check"

    def test_ping(self, client):
        res = client.get(self._url)
        assert res.status_code == status.HTTP_200_OK
