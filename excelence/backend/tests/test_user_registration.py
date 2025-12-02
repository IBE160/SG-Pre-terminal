from fastapi.testclient import TestClient
import pytest


def test_create_user_success(client):
    response = client.post(
        "/api/v1/users",
        json={"email": "test2@example.com", "password": "ValidPassword123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["token"]["access_token"]
    assert data["data"]["user"]["email"] == "test2@example.com"


def test_create_user_duplicate_email(client):
    # First user
    client.post(
        "/api/v1/users",
        json={"email": "test3@example.com", "password": "ValidPassword123"},
    )
    # Duplicate user
    response = client.post(
        "/api/v1/users",
        json={"email": "test3@example.com", "password": "ValidPassword123"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "The user with this email already exists in the system."
