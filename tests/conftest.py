from fastapi.testclient import TestClient
from url_shortener.api.endpoints.base import app
from url_shortener.db.repository import FakeRepositoryUrl
from url_shortener.service.url_service import UrlService
import pytest


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def fake_pg_service():
    return UrlService(None, FakeRepositoryUrl)

