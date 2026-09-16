from sqlalchemy import Column, Integer, String, Text

from apps.api.core.database import Base


class Thread(Base):

    __tablename__ = "threads"

    id = Column(Integer, primary_key=True, index=True)

    gmail_thread_id = Column(String, unique=True)

    subject = Column(String)

    summary = Column(Text, nullable=True)
