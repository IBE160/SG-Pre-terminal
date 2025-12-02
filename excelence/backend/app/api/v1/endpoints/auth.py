from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db.session import supabase

router = APIRouter()

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/signup")
def signup(user: UserCreate):
    """
    Create a new user.
    """
    try:
        res = supabase.auth.sign_up({
            "email": user.email,
            "password": user.password,
        })
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UserLogin):
    """
    Authenticate a user.
    """
    try:
        res = supabase.auth.sign_in_with_password({
            "email": user.email,
            "password": user.password,
        })
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))