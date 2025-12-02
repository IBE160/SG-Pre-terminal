from pydantic import BaseModel, EmailStr, validator
import re


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Za-z]', v):
            raise ValueError('Password must contain at least one letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one number')
        return v


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreateResponse(BaseModel):
    status: str
    data: dict[str, UserResponse | Token]

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
