from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
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

    # Связь с участием в турнирах
    participations = relationship("TournamentParticipant", back_populates="user")


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime(timezone=True), nullable=False)  # дата начала
    end_date = Column(DateTime(timezone=True), nullable=True)  # дата окончания
    chall_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    participants = relationship("TournamentParticipant", back_populates="tournament")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date.isoformat() if self.date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "chall_url": self.chall_url,
            "is_active": self.is_active,
        }


class TournamentParticipant(Base):
    __tablename__ = "tournament_participants"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    joined_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="participations")
    tournament = relationship("Tournament", back_populates="participants")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "tournament_id": self.tournament_id,
            "joined_at": self.joined_at.isoformat() if self.joined_at else None,
        }
