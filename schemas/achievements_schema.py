import datetime
import uuid
from typing import Optional

from .base_schema import BaseModel


class CreateAchievement(BaseModel):
    title: Optional[str]
    rating: Optional[str]
    game_id: str


class ReadAchievement(BaseModel):
    id: uuid.UUID
    title: Optional[str]
    rating: Optional[str]
    game_id: str
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdateAchievement(BaseModel):
    title: Optional[str]
    rating: Optional[str]
    game_id: str

    class Config:
        orm_mode = True
