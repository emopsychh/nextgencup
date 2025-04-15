from sqlalchemy import Column, BigInteger, String, DateTime, func
from bot_service.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String)
    first_name = Column(String)  # 👈 Имя пользователя
    last_name = Column(String)   # 👈 Фамилия пользователя
    steam_id = Column(String)
    created_at = Column(DateTime, default=func.now())
