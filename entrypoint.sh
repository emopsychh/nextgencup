#!/bin/sh

echo "⏳ Ждём базу данных..."

# ping PostgreSQL по хосту db:5432
while ! nc -z db 5432; do
  sleep 1
done

echo "✅ База данных доступна. Применяем миграции Alembic..."
alembic upgrade head

echo "🚀 Запускаем Telegram-бота..."
python bot_service/main.py