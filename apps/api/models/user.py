from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from apps.api.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False)

    provider = Column(String, default="gmail")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
