from fastapi import FastAPI
from sqlalchemy import text

from apps.api.core.database import engine
from apps.api.routes.gmail import router as gmail_router
from apps.api.routes.sync import router as sync_router

app = FastAPI(
    title="MailOps AI",
    version="0.1.0"
)

app.include_router(gmail_router)
app.include_router(sync_router)


@app.get("/")
async def root():
    return {
        "message": "MailOps AI API running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.get("/db-health")
async def db_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "connected"
        }

    except Exception as e:
        return {
            "database": "failed",
            "error": str(e)
        }
