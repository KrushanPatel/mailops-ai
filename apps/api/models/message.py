from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text

from pgvector.sqlalchemy import Vector

from apps.api.core.database import Base


class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    thread_id = Column(
        Integer,
        ForeignKey("threads.id")
    )

    sender = Column(Text)

    recipients = Column(Text)

    body = Column(Text)

    clean_body = Column(Text)

    embedding = Column(Vector(3072))
