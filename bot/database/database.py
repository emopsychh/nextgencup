import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from bot.config import Config
from bot.database.models import Base

# Создаём движок подключения к базе (URL берём из .env)
engine = create_async_engine(Config.DB_URL, echo=False)

# Создаём фабрику сессий (аналог "открыть соединение")
async_session = async_sessionmaker(engine, expire_on_commit=False)

# Функция создания таблиц (один раз при старте проекта)
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
