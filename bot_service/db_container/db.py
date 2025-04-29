from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator
from bot_service.config import DATABASE_URL

Base = declarative_base()

# ✅ Создаём движок через функцию
def get_engine():
    return create_async_engine(DATABASE_URL, echo=False)

# ✅ Создаём фабрику сессий через функцию
def get_session_factory():
    engine = get_engine()
    return async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
    )

# ✅ Генератор асинхронных сессий для FastAPI или работы в коде
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()
    async with session_factory() as session:
        yield session

# ✅ Оставляем отдельную фабрику для бота (если нужно)
AsyncSessionLocal = async_sessionmaker(
    bind=get_engine(),
    expire_on_commit=False,
)
