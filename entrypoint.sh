#!/bin/sh

echo "📦 Применяем миграции Alembic..."
alembic upgrade head

echo "🤖 Запускаем Telegram-бота..."
python -m bot_service.main
