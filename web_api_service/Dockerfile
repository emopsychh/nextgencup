FROM python:3.13-alpine

# Установка системных зависимостей
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    postgresql-dev \
    musl-dev \
    gcc \
    python3-dev

# Рабочая директория
WORKDIR /app

# Установка Python-зависимостей
COPY web_api_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir "uvicorn[standard]"

# Копирование кода проекта
COPY web_api_service ./web_api_service
COPY bot_service ./bot_service

# Копирование Alembic миграций
COPY bot_service/alembic ./alembic
COPY bot_service/alembic.ini ./alembic.ini

# Установка переменной окружения (для импорта модулей)
ENV PYTHONPATH=/app

# Команда запуска
CMD ["uvicorn", "web_api_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
