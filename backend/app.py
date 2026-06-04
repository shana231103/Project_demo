import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List, Optional
from schemas import UserProfile, SearchCriteria

app = FastAPI(title="My Project")

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASSWORD = "lolmht2003"
DB_NAME = "demo"

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursor_factory=RealDictCursor
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Cant connect to db"
        )

@app.get("/")
def read_root():
    return {"message": "/docs"}

@app.get("/players", response_model=List[UserProfile])
def get_all_players():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name, team, kda FROM user_profile;")
        players = cursor.fetchall()
        return players
    finally:
        cursor.close()
        conn.close()

@app.get("/search", response_model=List[UserProfile])
def search_players_get(
    name: str = Query(..., description="Nhap name")
):
    if not name or not name.strip():
        raise HTTPException(
            status_code=400,
            detail="Chua nhap name"
        )

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        
        query = "SELECT name, team, kda FROM user_profile WHERE name ILIKE %s"
        params = [f"%{name.strip()}%"]

        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()
        conn.close()

@app.post("/search", response_model=List[UserProfile])
def search_players_post(criteria: SearchCriteria):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()

        query = "SELECT name, team, kda FROM user_profile WHERE name ILIKE %s"
        params = [f"%{criteria.name}%"]

        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()
        conn.close()

