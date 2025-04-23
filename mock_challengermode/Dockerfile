FROM python:3.13-alpine
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pydantic
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]