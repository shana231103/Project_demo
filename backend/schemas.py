from pydantic import BaseModel, Field, field_validator

class SearchCriteria(BaseModel):
    name: str

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("Name khong duoc de trong hoac backspace")
        return normalized_value

    class Config:
        json_schema_extra = {
            "example": {
                "name": "shana"
            }
        }

class UserProfile(BaseModel):
    name: str
    team: str
    kda: float

    class Config:
        json_schema_extra = {
            "example": {
                "name": "proplayer1",
                "team": "team1",
                "kda": 2.0
            }
        }