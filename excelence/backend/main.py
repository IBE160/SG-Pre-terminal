from fastapi import FastAPI
from app.api.v1.endpoints import auth, items

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
