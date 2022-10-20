import datetime
import uuid
from typing import Optional

from .base_schema import BaseModel


class CreateUserAchievement(BaseModel):
    title: Optional[str]
    rating: Optional[str]
    user_id: str
    achievement_id: str
    user_game_id: str


class ReadUserAchievement(BaseModel):
    id: uuid.UUID
    title: Optional[str]
    rating: Optional[str]
    user_id: str
    achievement_id: str
    user_game_id: str
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdateUserAchievement(BaseModel):
    title: Optional[str]
    rating: Optional[str]
    user_id: str
    achievement_id: str
    user_game_id: str

    class Config:
        orm_mode = True
