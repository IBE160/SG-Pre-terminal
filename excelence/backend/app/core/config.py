import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    SUPABASE_URL: str
    SUPABASE_KEY: str

    class Config:
        case_sensitive = True
        env_file = 'excelence/backend/.env'
        env_file_encoding = 'utf-8'

settings = Settings()

