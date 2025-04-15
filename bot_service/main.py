import asyncio
from aiogram import Bot, Dispatcher
from bot_service.config import Config
from bot_service.database.database import create_tables
from bot_service.handlers import register

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
