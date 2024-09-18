import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def client():
    """APIのテスト用クライアント"""

    client = TestClient(app)
    return client
