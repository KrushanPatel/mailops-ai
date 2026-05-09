from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func

from apps.api.core.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    thread_id = Column(Integer, ForeignKey("threads.id"))

    sender = Column(String)

    recipients = Column(Text)

    body = Column(Text)

    clean_body = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
