from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()
fake_tournaments = {}

class TournamentCreate(BaseModel):
    name: str
    description: str
    game: str

@app.post("/tournaments")
async def create_tournament(tournament: TournamentCreate):
    tournament_id = str(uuid4())
    fake_tournaments[tournament_id] = tournament.dict()
    return {
        "tournament_id": tournament_id,
        "status": "created",
        "details": fake_tournaments[tournament_id],
    }
