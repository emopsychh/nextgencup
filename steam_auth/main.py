from fastapi import FastAPI, Request
from auth import start_steam_auth, handle_steam_response

app = FastAPI()

@app.get("/auth/steam")
async def steam_entry(tg_id: int):
    return await start_steam_auth(tg_id)

@app.get("/auth/steam/callback")
async def steam_callback(request: Request):
    return await handle_steam_response(request)
