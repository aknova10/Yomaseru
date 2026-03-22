from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func

from app.db.session import Base


class Vocab(Base):
    __tablename__ = "vocab"

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(Text, nullable=False)
    reading = Column(Text)
    jlpt_level = Column(String)

    created_at = Column(TIMESTAMP, server_default=func.now())


class SyncLog(Base):
    __tablename__ = "anki_sync_log"

    id = Column(Integer, primary_key=True, index=True)
    synced_at = Column(TIMESTAMP, server_default=func.now())
    total_fetched = Column(Integer)
    total_inserted = Column(Integer)