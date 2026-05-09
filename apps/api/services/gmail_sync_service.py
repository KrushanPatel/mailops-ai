from sqlalchemy.orm import Session

from apps.api.models.message import Message
from apps.api.models.thread import Thread

from packages.email_core.gmail_provider import build_gmail_service
from packages.email_core.parser import extract_email_body
from packages.email_core.sync_engine import fetch_threads


def sync_gmail_threads(db: Session):

    service = build_gmail_service()

    gmail_threads = fetch_threads()

    synced_count = 0
    synced_messages = 0

    for thread in gmail_threads:

        gmail_thread_id = thread["id"]

        existing_thread = db.query(Thread).filter(
            Thread.gmail_thread_id == gmail_thread_id
        ).first()

        if existing_thread:
            continue

        thread_data = service.users().threads().get(
            userId="me",
            id=gmail_thread_id
        ).execute()

        subject = ""

        messages = thread_data.get("messages", [])

        if messages:

            headers = messages[0]["payload"]["headers"]

            for header in headers:

                if header["name"] == "Subject":
                    subject = header["value"]
                    break

        db_thread = Thread(
            gmail_thread_id=gmail_thread_id,
            subject=subject
        )

        db.add(db_thread)
        db.flush()

        for gmail_message in messages:

            payload = gmail_message.get("payload", {})

            headers = payload.get("headers", [])

            sender = ""
            recipients = ""

            for header in headers:

                if header["name"] == "From":
                    sender = header["value"]

                if header["name"] == "To":
                    recipients = header["value"]

            clean_body = extract_email_body(payload)

            db_message = Message(
                thread_id=db_thread.id,
                sender=sender,
                recipients=recipients,
                body=clean_body,
                clean_body=clean_body
            )

            db.add(db_message)

            synced_messages += 1

        synced_count += 1

    db.commit()

    return {
        "synced_threads": synced_count,
        "synced_messages": synced_messages
    }
