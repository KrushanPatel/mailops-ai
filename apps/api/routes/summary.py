from fastapi import APIRouter
from sqlalchemy.orm import Session

from apps.api.core.database import SessionLocal

from apps.api.services.thread_summary_service import (
    summarize_threads
)

router = APIRouter(
    prefix="/summary",
    tags=["summary"]
)


@router.post("/threads")
async def summarize_email_threads():

    db: Session = SessionLocal()

    try:
        return summarize_threads(db)

    finally:
        db.close()
