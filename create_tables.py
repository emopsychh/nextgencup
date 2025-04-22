from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from datetime import datetime
import asyncio

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# Подключение к БД
DATABASE_URL = "postgresql+asyncpg://postgres:1231@db:5432/nextgencup"  

engine = create_async_engine(DATABASE_URL, echo=True)

async def create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create())
