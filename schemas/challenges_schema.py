import datetime
import uuid
from typing import Optional

from .base_schema import BaseModel


class CreateChallenge(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    location: Optional[str]
    date: Optional[datetime.date]
    time: Optional[str]
    user_id: str
    game_id: str


class ReadChallenge(BaseModel):
    id: uuid.UUID
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    location: Optional[str]
    date: Optional[datetime.date]
    time: Optional[str]
    user_id: str
    game_id: str
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdateChallenge(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    location: Optional[str]
    date: Optional[datetime.date]
    time: Optional[str]
    user_id: str
    game_id: str

    class Config:
        orm_mode = True
