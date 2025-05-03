FROM python:3.13-alpine

WORKDIR /app

# ставим зависимости из requirements
COPY web_api_service/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir "uvicorn[standard]"

# копируем весь проект целиком (чтобы внутри /app был и bot_service, и web_api_service и migrations)
COPY web_api_service ./web_api_service
COPY bot_service   ./bot_service
COPY migrations    ./migrations
COPY alembic.ini   .

# по-хорошему лишнее — но можно:
ENV PYTHONPATH=/app

CMD ["uvicorn", "web_api_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
 