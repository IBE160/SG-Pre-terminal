import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, PropertyMock
import uuid

# Mock user object that the get_current_user dependency would return
USER_ID = uuid.uuid4()

# Mock Supabase user object structure
class MockSupabaseUser:
    id = USER_ID

class MockUserResponse:
    user = MockSupabaseUser()

@pytest.fixture
def mock_supabase_auth(mocker):
    """Mocks the supabase auth get_user call in the new dependency location."""
    return mocker.patch(
        "app.api.deps.supabase.auth.get_user",
        return_value=MockUserResponse()
    )

@pytest.fixture
def mock_supabase_db(mocker):
    """Mocks the supabase table calls."""
    # We patch at the endpoint level as it's easier than patching the session import
    return mocker.patch("app.api.v1.endpoints.categories.supabase.table")


def test_create_category(client: TestClient, mock_supabase_auth, mock_supabase_db):
    mock_execute = MagicMock()
    type(mock_execute).data = PropertyMock(return_value=[{"id": 1, "name": "Groceries", "user_id": USER_ID}])
    mock_supabase_db.return_value.insert.return_value.execute.return_value = mock_execute

    response = client.post(
        "/api/v1/categories/",
        json={"name": "Groceries"},
        headers={"Authorization": "Bearer fake-token"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Groceries"
    assert data["id"] == 1
    assert data["user_id"] == str(USER_ID)

def test_read_categories(client: TestClient, mock_supabase_auth, mock_supabase_db):
    mock_execute = MagicMock()
    type(mock_execute).data = PropertyMock(return_value=[
        {"id": 1, "name": "Groceries", "user_id": str(USER_ID)},
        {"id": 2, "name": "Salary", "user_id": str(USER_ID)}
    ])
    mock_supabase_db.return_value.select.return_value.eq.return_value.order.return_value.execute.return_value = mock_execute

    response = client.get(
        "/api/v1/categories/",
        headers={"Authorization": "Bearer fake-token"}
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Groceries"

def test_update_category(client: TestClient, mock_supabase_auth, mock_supabase_db):
    mock_execute = MagicMock()
    type(mock_execute).data = PropertyMock(return_value=[{"id": 1, "name": "Food", "user_id": str(USER_ID)}])
    mock_supabase_db.return_value.update.return_value.eq.return_value.eq.return_value.execute.return_value = mock_execute

    response = client.put(
        "/api/v1/categories/1",
        json={"name": "Food"},
        headers={"Authorization": "Bearer fake-token"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Food"

def test_delete_category_success(client: TestClient, mock_supabase_auth, mock_supabase_db):
    # Mock transaction check (no transactions found)
    mock_transaction_check = MagicMock()
    type(mock_transaction_check).count = PropertyMock(return_value=0)
    
    # Mock delete call
    mock_delete_execute = MagicMock()
    type(mock_delete_execute).data = PropertyMock(return_value=[{"id": 1}])

    # Configure the mock_supabase_db to handle both calls
    mock_supabase_db.return_value.select.return_value.eq.return_value.eq.return_value.execute.return_value = mock_transaction_check
    mock_supabase_db.return_value.delete.return_value.eq.return_value.eq.return_value.execute.return_value = mock_delete_execute
    
    response = client.delete(
        "/api/v1/categories/1",
        headers={"Authorization": "Bearer fake-token"}
    )
    
    assert response.status_code == 200
    assert response.json() == {"detail": "Category deleted successfully"}

def test_delete_category_in_use(client: TestClient, mock_supabase_auth, mock_supabase_db):
    # Mock transaction check (1 transaction found)
    mock_transaction_check = MagicMock()
    type(mock_transaction_check).count = PropertyMock(return_value=1)
    mock_supabase_db.return_value.select.return_value.eq.return_value.eq.return_value.execute.return_value = mock_transaction_check

    response = client.delete(
        "/api/v1/categories/1",
        headers={"Authorization": "Bearer fake-token"}
    )

    assert response.status_code == 400
    assert "Cannot delete category" in response.json()["detail"]

def test_update_category_not_found(client: TestClient, mock_supabase_auth, mock_supabase_db):
    mock_execute = MagicMock()
    type(mock_execute).data = PropertyMock(return_value=[]) # Simulate no record found
    mock_supabase_db.return_value.update.return_value.eq.return_value.eq.return_value.execute.return_value = mock_execute

    response = client.put(
        "/api/v1/categories/999",
        json={"name": "Food"},
        headers={"Authorization": "Bearer fake-token"}
    )

    assert response.status_code == 404
    assert "Category not found" in response.json()["detail"]
