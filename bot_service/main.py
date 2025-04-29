import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aiogram import Bot, Dispatcher
from bot_service.config import BOT_TOKEN
from bot_service.db_container.db import Base
from bot_service.db_container.db import get_session
from bot_service.handlers import routers, start, profile, tournaments, settings


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
for router in routers:
    dp.include_router(router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())