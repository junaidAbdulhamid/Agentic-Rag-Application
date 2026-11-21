from fastapi import FastAPI

from app.core.api.routes.health import router as health_router
from app.core.config import get_settings


settings = get_settings()
app = FastAPI(title=settings.APP_NAME, version="0.1.0")
app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Agentic RAG API is running"}
