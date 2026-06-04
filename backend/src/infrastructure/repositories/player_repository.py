"""
Infrastructure Layer - Concrete Repository
Triển khai IPlayerRepository bằng Postgres thực tế.
Domain layer không biết file này tồn tại.
"""

from typing import List
from domain.user_profile import UserProfile
from domain.player_repository_interface import IPlayerRepository
from infrastructure.database import get_db


class PostgresPlayerRepository(IPlayerRepository):

    def get_all(self) -> List[UserProfile]:
        with get_db() as cursor:
            cursor.execute("SELECT name, team, kda FROM user_profile;")
            rows = cursor.fetchall()
        return [UserProfile(name=r["name"], team=r["team"], kda=r["kda"]) for r in rows]

    def search_by_name(self, name: str) -> List[UserProfile]:
        with get_db() as cursor:
            cursor.execute(
                "SELECT name, team, kda FROM user_profile WHERE name ILIKE %s",
                [f"%{name}%"],
            )
            rows = cursor.fetchall()
        return [UserProfile(name=r["name"], team=r["team"], kda=r["kda"]) for r in rows]
