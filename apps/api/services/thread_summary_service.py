from sqlalchemy.orm import Session

from apps.api.models.thread import Thread
from apps.api.models.message import Message

from packages.llm_router.factory import (
    get_chat_provider
)

chat_provider = get_chat_provider()


def summarize_threads(db: Session):

    threads = db.query(Thread).filter(
        Thread.summary == None
    ).all()

    summarized_count = 0

    for thread in threads:

        messages = db.query(Message).filter(
            Message.thread_id == thread.id
        ).all()

        combined_text = "\n\n".join([
            msg.clean_body or ""
            for msg in messages
        ])

        if not combined_text.strip():
            continue

        prompt = f"""
        Summarize this email thread in 2 concise sentences.

        Email Thread:
        {combined_text[:12000]}
        """

        summary = chat_provider.generate(prompt)

        thread.summary = summary

        summarized_count += 1

    db.commit()

    return {
        "summarized_threads": summarized_count
    }
