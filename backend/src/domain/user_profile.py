from dataclasses import dataclass


@dataclass(frozen=True)
class UserProfile:
    name: str
    team: str
    kda: float

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Tên người chơi không được để trống.")
        if not self.team or not self.team.strip():
            raise ValueError("Tên đội không được để trống.")
        if self.kda < 0:
            raise ValueError("KDA không thể âm.")

    @property
    def is_high_performer(self) -> bool:
        return self.kda >= 3.0

    @property
    def performance_tier(self) -> str:
        if self.kda >= 5.0:
            return "Legend"
        elif self.kda >= 3.0:
            return "Diamond"
        elif self.kda >= 2.0:
            return "Gold"
        else:
            return "Bronze"
