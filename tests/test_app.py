from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_demo_markets_cannot_be_mistaken_for_live():
    response = client.get("/api/markets")
    assert response.status_code == 200
    data = response.json()
    assert data["mode"] == "demo"
    assert "FICTIONAL" in data["disclaimer"]
    assert "as_of_utc" not in data
    assert len(data["instruments"]) == 4

def test_pages_available():
    for path in ("/", "/scene"):
        response = client.get(path)
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]

def test_scene_displays_demo_warning():
    response = client.get("/scene")
    assert "DEMO — NOT LIVE DATA" in response.text
    assert "Broadcast offline" in response.text
