from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_get_devices():

    response = client.get("/devices")

    assert response.status_code == 200

    assert isinstance(response.json(), list)