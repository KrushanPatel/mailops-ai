from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from apps.api.core.database import get_db
from apps.api.services.gmail_sync_service import sync_gmail_threads

router = APIRouter()


@router.post("/sync/gmail")
async def gmail_sync(
    db: Session = Depends(get_db)
):

    result = sync_gmail_threads(db)

    return result
