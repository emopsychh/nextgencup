from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from bot_service.config import DATABASE_URL
from typing import AsyncGenerator

# Асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=False)

# Асинхронная сессия
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

# Базовый класс для моделей
Base = declarative_base()

# Генератор асинхронных сессий
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
