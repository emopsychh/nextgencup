import sys
import pathlib

from fastapi import FastAPI, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# чтобы py-path начинался с корня репозитория
ROOT = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT))

from bot_service.db_container.models import Tournament, User
from bot_service.db_container.db import async_session, get_session

app = FastAPI()


@app.get("/tournaments")
async def get_tournaments(session: AsyncSession = Depends(get_session)):
    # используем get_session, а не raw async_session
    result = await session.execute(select(Tournament))
    tournaments = result.scalars().all()
    return [t.to_dict() for t in tournaments]


@app.get("/profile")
async def get_profile(
    x_telegram_id: int = Header(..., alias="X-Telegram-ID"),
    session: AsyncSession = Depends(get_session),
):
    # ищем пользователя по telegram_id
    result = await session.execute(
        select(User).where(User.telegram_id == x_telegram_id)
    )
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "username": user.username or "",
        "photoUrl": user.photo_url or ""
    }
