from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.db import engine, Base
from handlers import routers


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

for router in routers:
    dp.include_router(router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())