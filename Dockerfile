FROM python:3.13-alpine

RUN apk add --no-cache netcat-openbsd bash postgresql-dev gcc python3-dev musl-dev libffi-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
