import pytest
from fastapi.testclient import TestClient
import sys
import os
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

# Set test environment variables before importing app
os.environ["TESTING"] = "true"
os.environ.setdefault("SECRET_KEY", "test_secret_key_for_testing_only")

from main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c