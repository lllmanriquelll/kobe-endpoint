from fastapi.testclient import TestClient
from kobe.main import app

client = TestClient(app)


def test_header_key_value():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["kobe-endpoint"] == "omnivector"
