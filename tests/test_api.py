from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert "status" in data
    assert "cpu_usage" in data
    assert "memory_usage" in data
    assert "disk_usage" in data


def test_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200

    data = response.json()

    assert "cpu_usage" in data
    assert "memory_usage" in data
    assert "disk_usage" in data
    assert "network" in data


def test_alerts():
    response = client.get("/alerts")

    assert response.status_code == 200

    data = response.json()

    assert "alerts" in data
    assert "count" in data
    assert "healing_results" in data
