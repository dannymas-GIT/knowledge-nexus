from fastapi import FastAPI

from app.api.routes.health import router as health_router

app = FastAPI()

app.include_router(health_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Knowledge Nexus API"} 