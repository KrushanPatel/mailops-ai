from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from apps.api.core.database import get_db

from apps.api.services.semantic_search_service import (
    index_message_embeddings,
    semantic_search
)

router = APIRouter()


@router.post("/embeddings/index")
async def index_embeddings(
    db: Session = Depends(get_db)
):

    return index_message_embeddings(db)


@router.get("/search")
async def search_emails(
    query: str,
    db: Session = Depends(get_db)
):

    return semantic_search(
        db,
        query
    )
