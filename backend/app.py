from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from schemas import UserProfile, SearchCriteria
from database import get_db

app = FastAPI(title="My Project")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "/docs"}

@app.get("/players", response_model=List[UserProfile])
def get_all_players():
    with get_db() as cursor:
        cursor.execute("SELECT name, team, kda FROM user_profile;")
        return cursor.fetchall()

@app.get("/search", response_model=List[UserProfile])
def search_players_get(
    name: str = Query(..., description="Nhap name")
):
    search_name = name.strip()
    if not search_name:
        raise HTTPException(status_code=400, detail="Name khong duoc de trong")

    with get_db() as cursor:
        query = "SELECT name, team, kda FROM user_profile WHERE name ILIKE %s"
        cursor.execute(query, [f"%{search_name}%"])
        return cursor.fetchall()

@app.post("/search", response_model=List[UserProfile])
def search_players_post(criteria: SearchCriteria):
    with get_db() as cursor:
        query = "SELECT name, team, kda FROM user_profile WHERE name ILIKE %s"
        cursor.execute(query, [f"%{criteria.name}%"])
        return cursor.fetchall()