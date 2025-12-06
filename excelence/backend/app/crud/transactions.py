import uuid
from app.db.session import supabase

def delete_transaction(transaction_id: uuid.UUID, user_id: uuid.UUID) -> bool:
    """
    Deletes a transaction by its ID for a specific user.
    Returns True if deletion was successful (record found and deleted), False otherwise.
    """
    response = supabase.table('transactions').delete().match({
        'id': str(transaction_id),
        'user_id': str(user_id)
    }).execute()

    if response.data:
        return True
    return False
