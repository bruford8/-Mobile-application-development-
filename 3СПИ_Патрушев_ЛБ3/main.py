import uvicorn
from fastapi import FastAPI

from api.v1.router import router as api_v1_router

app = FastAPI(title="Books & Movies API", version="1.0")

app.include_router(api_v1_router, prefix="/api")


@app.get("/")
def read_root():
    return {"docs": "/docs", "api": "/api/v1"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)