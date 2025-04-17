# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from db_container.db import engine, Base
from handlers import routers, start, profile, tournaments, settings


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
for router in routers:
    dp.include_router(router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())