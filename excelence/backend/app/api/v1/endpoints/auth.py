from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.user import UserCreate, UserCreateResponse, UserResponse, Token


router = APIRouter()


@router.post("/users", response_model=UserCreateResponse)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
):
    """
    Create new user.
    """
    user = crud.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud.create_user(db, obj_in=user_in)
    token = Token(
        access_token=create_access_token(user.id),
        token_type="bearer",
    )
    return {
        "status": "success",
        "data": {
            "user": UserResponse.from_orm(user),
            "token": token,
        },
    }
