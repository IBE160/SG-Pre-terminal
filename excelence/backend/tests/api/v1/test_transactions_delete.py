import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, PropertyMock
import uuid

USER_ID = uuid.uuid4()

class MockSupabaseUser:
    id = USER_ID

class MockUserResponse:
    user = MockSupabaseUser()

@pytest.fixture
def mock_supabase_auth(mocker):
    return mocker.patch(
        "app.api.deps.supabase.auth.get_user",
        return_value=MockUserResponse()
    )

@pytest.fixture
def mock_crud_supabase(mocker):
    # Mocking the supabase client used in the crud module
    return mocker.patch("app.crud.transactions.supabase.table")

def test_delete_transaction_success(client: TestClient, mock_supabase_auth, mock_crud_supabase):
    mock_execute = MagicMock()
    # Return a list with one item to simulate successful deletion
    type(mock_execute).data = PropertyMock(return_value=[{"id": str(uuid.uuid4())}])
    
    mock_crud_supabase.return_value.delete.return_value.match.return_value.execute.return_value = mock_execute
    
    transaction_id = uuid.uuid4()
    response = client.delete(
        f"/api/v1/transactions/{transaction_id}",
        headers={"Authorization": "Bearer fake-token"}
    )
    
    assert response.status_code == 200
    assert response.json() == {"detail": "Transaction deleted successfully"}
    
    # Verify the correct calls were made
    mock_crud_supabase.assert_called_with('transactions')
    mock_crud_supabase.return_value.delete.assert_called_once()
    mock_crud_supabase.return_value.delete.return_value.match.assert_called_with({
        'id': str(transaction_id),
        'user_id': str(USER_ID)
    })

def test_delete_transaction_not_found(client: TestClient, mock_supabase_auth, mock_crud_supabase):
    mock_execute = MagicMock()
    # Return empty list to simulate not found or not owned by user
    type(mock_execute).data = PropertyMock(return_value=[])
    
    mock_crud_supabase.return_value.delete.return_value.match.return_value.execute.return_value = mock_execute
    
    transaction_id = uuid.uuid4()
    response = client.delete(
        f"/api/v1/transactions/{transaction_id}",
        headers={"Authorization": "Bearer fake-token"}
    )
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Transaction not found or user does not have permission."}
