# create_tables.py
import asyncio

from bot_service.db_container.db import engine, Base

async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("✅ Таблицы успешно созданы вручную.")

if __name__ == "__main__":
    asyncio.run(create_all())
