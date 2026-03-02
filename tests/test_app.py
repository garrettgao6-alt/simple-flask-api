import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app


def test_home():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    app = create_app()
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
