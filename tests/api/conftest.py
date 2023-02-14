import pytest
import json
from starlette import status
from fastapi.testclient import TestClient
from url_shortener.api.endpoints.base import app
from url_shortener.service import Config


@pytest.fixture(scope="session")
def service_config():
    Config.fake = True
    conf = Config()
    yield conf


@pytest.fixture
def client(service_config):
    client = TestClient(app)
    return client


@pytest.fixture
def suffix_body(client):
    to_make_shorter = "https://www.python.org"
    i_body = {"long_url": to_make_shorter}
    res = client.post("/url/v1", data=json.dumps(i_body))
    assert res.status_code == status.HTTP_200_OK
    body = res.json()
    assert "suffix" in body.keys()
    return body
