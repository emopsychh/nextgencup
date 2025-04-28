from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/tournaments")
async def create_tournament(request: Request):
    print("✅ MOCK API ПОЛУЧИЛ ЗАПРОС НА СОЗДАНИЕ ТУРНИРА")
    body = await request.json()
    print("📦 Данные запроса:", body)

    return JSONResponse(content={
        "tournament_id": "mock-tournament-id"
    })


@app.post("/oauth/token")
async def fake_oauth_token():
    print("🔐 Перехватили запрос на авторизацию Challengermode!")

    return JSONResponse(content={
        "access_token": "mocked-access-token",
        "token_type": "bearer",
        "expires_in": 3600
    })
