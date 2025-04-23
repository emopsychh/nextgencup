from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean
from sqlalchemy.sql import func
from bot_service.db_container.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    username = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Будущие поля
    games_played = Column(Integer, default=0)
    games_won = Column(Integer, default=0)

class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime(timezone=True), nullable=False)
    chall_url = Column(String, nullable=True)  # ссылка на Challengermode
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date.isoformat() if self.date else None,
            "chall_url": self.chall_url,
            "is_active": self.is_active,
        }