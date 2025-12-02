from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.main import app
from app.api import deps
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[deps.get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="function")
def db_session():
    # setup
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    # teardown
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_user_success(db_session):
    response = client.post(
        "/api/v1/users",
        json={"email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "access_token" in data["data"]
    assert data["data"]["user"]["email"] == "test@example.com"


def test_create_user_duplicate_email(db_session):
    # First user
    client.post(
        "/api/v1/users",
        json={"email": "test@example.com", "password": "password123"},
    )
    # Duplicate user
    response = client.post(
        "/api/v1/users",
        json={"email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "The user with this username already exists in the system."
