from sqlalchemy import text
from sqlalchemy.orm import Session

from apps.api.models.message import Message

from packages.llm_router.factory import (
    get_embedding_provider
)

embedding_provider = get_embedding_provider()


def index_message_embeddings(db: Session):

    messages = db.query(Message).filter(
        Message.embedding == None
    ).all()

    indexed_count = 0

    for message in messages:

        if not message.clean_body:
            continue

        embedding = embedding_provider.embed_query(
            message.clean_body[:4000]
        )

        if not embedding:
            continue

        message.embedding = embedding

        indexed_count += 1

    db.commit()

    return {
        "indexed_messages": indexed_count
    }


def semantic_search(
    db: Session,
    query: str
):

    query_embedding = embedding_provider.embed_query(query)

    embedding_literal = "[" + ",".join(str(x) for x in query_embedding) + "]"

    sql = text("""
        SELECT
            id,
            clean_body,
            embedding <=> CAST(:embedding AS vector) AS distance
        FROM messages
        WHERE embedding IS NOT NULL
        ORDER BY distance
        LIMIT 5
    """)

    results = db.execute(
        sql,
        {
            "embedding": embedding_literal
        }
    )

    return [
        dict(row._mapping)
        for row in results
    ]
