from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from bot_service.config import Config

DATABASE_URL = Config.DB_URL

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

from bot_service.database.models import User  # ⚠️ Импортируй модель

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)