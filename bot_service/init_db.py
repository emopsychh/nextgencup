import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from bot_service.db_container import models
from bot_service.db_container.db import engine, Base

# Создаем сессию для работы с базой данных
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init():
    async with engine.begin() as conn:
        # Создаём все таблицы
        await conn.run_sync(Base.metadata.create_all)

    print("✅ База данных и таблицы успешно созданы!")

if __name__ == "__main__":
    asyncio.run(init())
