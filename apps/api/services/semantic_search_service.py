from sqlalchemy import text
from sqlalchemy.orm import Session

from apps.api.models.message import Message

from packages.llm_router.openai_embeddings import generate_embedding


def index_message_embeddings(db: Session):

    messages = db.query(Message).filter(
        Message.embedding == None
    ).all()

    indexed_count = 0

    for message in messages:

        if not message.clean_body:
            continue

        embedding = generate_embedding(
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

    query_embedding = generate_embedding(query)

    sql = text("""
        SELECT
            id,
            clean_body,
            embedding <=> :embedding AS distance
        FROM messages
        WHERE embedding IS NOT NULL
        ORDER BY distance
        LIMIT 5
    """)

    results = db.execute(
        sql,
        {
            "embedding": query_embedding
        }
    )

    return [
        dict(row._mapping)
        for row in results
    ]
