import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, PropertyMock
import uuid
from datetime import date

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
    return mocker.patch("app.api.v1.endpoints.transactions.supabase.table")


def test_create_transaction(client: TestClient, mock_supabase_auth, mock_supabase_db):
    mock_execute = MagicMock()
    today = date.today()
    type(mock_execute).data = PropertyMock(return_value=[{
        "id": 1,
        "amount": 50.0,
        "type": "expense",
        "date": str(today),
        "description": "Groceries",
        "user_id": USER_ID,
        "category_id": 1
    }])
    mock_supabase_db.return_value.insert.return_value.execute.return_value = mock_execute

    response = client.post(
        "/api/v1/transactions/",
        json={
            "amount": 50.0,
            "type": "expense",
            "date": str(today),
            "description": "Groceries",
            "category_id": 1
        },
        headers={"Authorization": "Bearer fake-token"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 50.0
    assert data["type"] == "expense"
    assert data["description"] == "Groceries"
    assert data["user_id"] == str(USER_ID)
    assert data["category_id"] == 1
