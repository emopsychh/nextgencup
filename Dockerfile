FROM python:3.13-alpine

# Установка зависимостей
RUN apk add --no-cache \
    netcat-openbsd \
    bash \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    libpq

# Рабочая директория
WORKDIR /app

# Установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всех файлов проекта
COPY . .

# Даем права на выполнение entrypoint
RUN chmod +x /app/entrypoint.sh

# Запуск контейнера через entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
