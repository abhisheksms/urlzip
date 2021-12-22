import pytest
from starlette.testclient import TestClient

@pytest.fixture(scope="session")
def test_app():
    from src.api import app
    client = TestClient(app)
    yield client