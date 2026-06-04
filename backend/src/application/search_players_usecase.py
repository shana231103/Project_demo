"""
Application Layer - Use Cases
Chứa logic nghiệp vụ của ứng dụng. Gọi domain entities và repository interfaces.
Không biết gì về FastAPI, HTTP hay Postgres.
"""

from typing import List
from domain.user_profile import UserProfile
from domain.player_repository_interface import IPlayerRepository


class GetAllPlayersUseCase:
    """Use case: lấy toàn bộ danh sách người chơi."""

    def __init__(self, repository: IPlayerRepository):
        self._repository = repository

    def execute(self) -> List[UserProfile]:
        return self._repository.get_all()


class SearchPlayersUseCase:
    """Use case: tìm kiếm người chơi theo tên."""

    def __init__(self, repository: IPlayerRepository):
        self._repository = repository

    def execute(self, name: str) -> List[UserProfile]:
        name = name.strip()
        if not name:
            raise ValueError("Tên tìm kiếm không được để trống.")
        return self._repository.search_by_name(name)
