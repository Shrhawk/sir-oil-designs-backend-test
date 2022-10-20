import datetime
import uuid
from typing import Optional

from .base_schema import BaseModel


class CreateUserGame(BaseModel):
    status: Optional[str]
    score: Optional[str]
    user_id: str
    game_id: str


class ReadUserGame(BaseModel):
    id: uuid.UUID
    status: Optional[str]
    score: Optional[str]
    user_id: str
    game_id: str
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdateUserGame(BaseModel):
    status: Optional[str]
    score: Optional[str]
    user_id: str
    game_id: str

    class Config:
        orm_mode = True
