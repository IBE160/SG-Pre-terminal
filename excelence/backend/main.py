from fastapi import FastAPI
from app.api.v1.endpoints import auth
from app.db.init_db import init_db
from app.db.session import SessionLocal
import os

# Only initialize database if not in test mode
if os.getenv("TESTING") != "true":
    init_db(SessionLocal())

app = FastAPI()


app.include_router(auth.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"Hello": "World"}
