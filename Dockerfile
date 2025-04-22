FROM python:3.13-alpine

# Установка зависимостей системы (bash, netcat, psycopg2)
RUN apk add --no-cache netcat-openbsd bash postgresql-dev gcc python3-dev musl-dev libffi-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем Python-пакеты
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Даем права на запуск entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Запуск через скрипт
ENTRYPOINT ["/app/entrypoint.sh"]
