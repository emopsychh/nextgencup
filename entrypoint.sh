#!/bin/sh

# Ожидание базы данных
echo "⏳ Waiting for db..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "✅ DB is up!"

# Применяем миграции
alembic -c bot_service/alembic.ini upgrade head

# Запуск Python-приложения
exec python bot_service/main.py
