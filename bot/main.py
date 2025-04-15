import asyncio
from aiogram import Bot, Dispatcher
from bot.config import Config
from bot.database.database import create_tables
from bot.handlers import register
from bot.handlers import menu, tournaments
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.config import Config

bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(menu.router)
dp.include_router(tournaments.router)

async def main():
    # Создаём бота и диспетчер
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем обработчики
    dp.include_router(register.router)

    # Создаём таблицы в БД (один раз)
    await create_tables()

    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
