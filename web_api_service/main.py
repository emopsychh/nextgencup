from fastapi import FastAPI
from bot_service.db_container.models import Tournament
from bot_service.db_container.db import async_session
from sqlalchemy.future import select

app = FastAPI()

@app.get("/tournaments")
async def get_tournaments():
    async with async_session() as session:
        result = await session.execute(select(Tournament))
        tournaments = result.scalars().all()
        return [t.to_dict() for t in tournaments]
