import pytest
from fastapi.testclient import TestClient
from url_shortener.api.endpoints.base import app
from url_shortener.config import get_settings
from url_shortener.service import fake_url_service, fake_auth_service


@pytest.fixture(scope='session')
def settings():
    return get_settings()


@pytest.fixture(scope='session')
def client(settings):
    client = TestClient(app)
    return client
