from starlette import status
import json


class TestUrl:
    to_make_shorter = "https://www.python.org"
    _url = "/url/v1"

    def test_main_scenario(self, client):
        i_body = {"long_url": self.to_make_shorter}
        res = client.post(self._url, data=json.dumps(i_body))
        assert res.status_code == status.HTTP_200_OK

    def test_unconnectable_url(self, client):
        i_body = {"long_url": self.to_make_shorter + "ddd"}
        res = client.post(self._url, data=json.dumps(i_body))
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_unreachable_url(self, client):
        i_body = {"long_url": self.to_make_shorter + "/facts6666"}
        res = client.post(self._url, data=json.dumps(i_body))
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_wrong_url_format(self, client):
        i_body = {"long_url": "definetly_not_a_URL"}
        res = client.post(self._url, data=json.dumps(i_body))
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
