from fastapi.testclient import TestClient
import pytest


def test_create_user_success(client):
    response = client.post(
        "/api/v1/users",
        json={"email": "test2@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "access_token" in data["data"]
    assert data["data"]["user"]["email"] == "test2@example.com"


def test_create_user_duplicate_email(client):
    # First user
    client.post(
        "/api/v1/users",
        json={"email": "test3@example.com", "password": "password123"},
    )
    # Duplicate user
    response = client.post(
        "/api/v1/users",
        json={"email": "test3@example.com", "password": "password123"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "The user with this username already exists in the system."
