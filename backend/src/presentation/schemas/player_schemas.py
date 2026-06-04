"""
Presentation Layer - Schemas
Pydantic models cho HTTP request/response.
Tách biệt hoàn toàn với Domain entities.
"""

from pydantic import BaseModel, Field, field_validator


class SearchCriteria(BaseModel):
    name: str

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("Name không được để trống hoặc chỉ là khoảng trắng.")
        return normalized

    model_config = {
        "json_schema_extra": {
            "example": {"name": "shana"}
        }
    }


class UserProfileResponse(BaseModel):
    """Response DTO — tách biệt với Domain entity UserProfile."""
    name: str
    team: str
    kda: float
    performance_tier: str = Field(default="Bronze", description="Tier dựa trên KDA")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "proplayer1",
                "team": "team1",
                "kda": 2.0,
                "performance_tier": "Gold",
            }
        }
    }
