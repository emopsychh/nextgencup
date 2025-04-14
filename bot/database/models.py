from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String, nullable=True)
    steam_id = Column(String, nullable=True)  # на будущее
    created_at = Column(DateTime, default=datetime.utcnow)