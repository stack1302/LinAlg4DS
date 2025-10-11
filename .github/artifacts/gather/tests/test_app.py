from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)
def test_health(): assert c.get("/health").json()["status"] == "ok"
def test_item(): assert c.get("/items/7").json()["id"] == 7
