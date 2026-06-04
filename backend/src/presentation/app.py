"""
Presentation Layer - FastAPI Application
Wires everything together: dependency injection, routing, middleware.
Chỉ layer này được phép biết về FastAPI.
"""

import sys
import os

# Thêm src vào path để import các module nội bộ
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from domain.user_profile import UserProfile as DomainUserProfile
from application.search_players_usecase import GetAllPlayersUseCase, SearchPlayersUseCase
from infrastructure.repositories.player_repository import PostgresPlayerRepository
from presentation.schemas.player_schemas import UserProfileResponse, SearchCriteria


app = FastAPI(
    title="Player Stats API",
    description="API quản lý thống kê người chơi — DDD + Clean Architecture",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Dependency Injection ────────────────────────────────────────────────────

def get_player_repository() -> PostgresPlayerRepository:
    return PostgresPlayerRepository()


def get_all_players_usecase(
    repo: PostgresPlayerRepository = Depends(get_player_repository),
) -> GetAllPlayersUseCase:
    return GetAllPlayersUseCase(repo)


def get_search_players_usecase(
    repo: PostgresPlayerRepository = Depends(get_player_repository),
) -> SearchPlayersUseCase:
    return SearchPlayersUseCase(repo)


# ─── Mapper: Domain → Response DTO ──────────────────────────────────────────

def to_response(player: DomainUserProfile) -> UserProfileResponse:
    return UserProfileResponse(
        name=player.name,
        team=player.team,
        kda=player.kda,
        performance_tier=player.performance_tier,
    )


# ─── Routes ─────────────────────────────────────────────────────────────────

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Player Stats API v2 — truy cập /docs để xem tài liệu."}


@app.get("/players", response_model=List[UserProfileResponse], tags=["Players"])
def get_all_players(
    use_case: GetAllPlayersUseCase = Depends(get_all_players_usecase),
):
    """Lấy toàn bộ danh sách người chơi."""
    players = use_case.execute()
    return [to_response(p) for p in players]


@app.get("/search", response_model=List[UserProfileResponse], tags=["Search"])
def search_players_get(
    name: str = Query(..., description="Tên người chơi cần tìm"),
    use_case: SearchPlayersUseCase = Depends(get_search_players_usecase),
):
    """Tìm kiếm người chơi qua GET query param."""
    try:
        players = use_case.execute(name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return [to_response(p) for p in players]


@app.post("/search", response_model=List[UserProfileResponse], tags=["Search"])
def search_players_post(
    criteria: SearchCriteria,
    use_case: SearchPlayersUseCase = Depends(get_search_players_usecase),
):
    """Tìm kiếm người chơi qua POST body (JSON)."""
    try:
        players = use_case.execute(criteria.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return [to_response(p) for p in players]
