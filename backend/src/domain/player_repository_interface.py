from abc import ABC, abstractmethod
from typing import List
from domain.user_profile import UserProfile


class IPlayerRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[UserProfile]:
        """Lấy toàn bộ danh sách người chơi."""
        ...

    @abstractmethod
    def search_by_name(self, name: str) -> List[UserProfile]:
        """Tìm kiếm người chơi theo tên (ILIKE)."""
        ...
