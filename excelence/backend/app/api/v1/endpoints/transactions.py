from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from app.db.session import supabase
from app.api import deps
import uuid
from datetime import date

router = APIRouter()

# --- Pydantic Models ---
class TransactionCreate(BaseModel):
    amount: float
    type: str  # "income" or "expense"
    date: date
    description: Optional[str] = None
    category_id: uuid.UUID

class Transaction(BaseModel):
    id: uuid.UUID
    amount: float
    type: str
    date: date
    description: Optional[str] = None
    user_id: uuid.UUID
    category_id: uuid.UUID

# --- API Endpoints ---
@router.post("/", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, user: dict = Depends(deps.get_current_user)):
    """
    Create a new transaction for the current user.
    """
    try:
        user_id = user.user.id
        response = supabase.table('transactions').insert({
            "amount": transaction.amount,
            "type": transaction.type,
            "date": str(transaction.date),
            "description": transaction.description,
            "category_id": transaction.category_id,
            "user_id": user_id
        }).execute()

        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create transaction.")

        created_transaction = response.data[0]
        return Transaction(**created_transaction)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
