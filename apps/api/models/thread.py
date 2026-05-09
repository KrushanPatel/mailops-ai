from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from apps.api.core.database import Base


class Thread(Base):
    __tablename__ = "threads"

    id = Column(Integer, primary_key=True, index=True)

    gmail_thread_id = Column(String, unique=True, nullable=False)

    subject = Column(String)

    summary = Column(String)

    priority_score = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
