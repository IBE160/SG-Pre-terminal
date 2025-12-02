from fastapi.testclient import TestClient


def test_create_user_success(client: TestClient):
    response = client.post(
        "/api/v1/users",
        json={"email": "test@example.com", "password": "ValidPassword123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["token"]["access_token"]
    assert data["data"]["user"]["email"] == "test@example.com"


def test_create_user_existing_email(client: TestClient):
    # First, create a user
    client.post(
        "/api/v1/users",
        json={"email": "test1@example.com", "password": "ValidPassword123"},
    )

    # Then, try to create another user with the same email
    response = client.post(
        "/api/v1/users",
        json={"email": "test1@example.com", "password": "ValidPassword123"},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "The user with this email already exists in the system."
