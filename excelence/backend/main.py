from fastapi import FastAPI
from app.api.v1.endpoints import auth, items, categories

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])



@app.get("/")
def read_root():
    return {"Hello": "World"}
