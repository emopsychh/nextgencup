# create_tables.py

from bot_service.db_container.db import engine, Base
import asyncio

async def create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create())
