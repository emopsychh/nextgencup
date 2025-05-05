# bot_service/main.py

import pathlib, sys
from aiogram import Bot, Dispatcher

# разрешаем импорт из корня репозитория
ROOT = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT))

from bot_service.config import BOT_TOKEN
from bot_service.handlers import routers
    
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# подключаем роутеры
for router in routers:
    dp.include_router(router)

async def main():
    # убираем вебхук, если был
    await bot.delete_webhook(drop_pending_updates=True)
    # запускаем polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
