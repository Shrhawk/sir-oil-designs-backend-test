import datetime
from typing import Optional

from .base_schema import BaseModel


class CreateEvent(BaseModel):
    title: Optional[str]
    description: Optional[str]
    location: Optional[str]
    date: Optional[str]
    time: Optional[str]
    public: Optional[bool]
    user_id: str
    game_id: str


class ReadEvent(BaseModel):
    title: Optional[str]
    description: Optional[str]
    location: Optional[str]
    date: Optional[str]
    time: Optional[str]
    public: Optional[bool]
    user_id: str
    game_id: str
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdateEvent(BaseModel):
    title: Optional[str]
    description: Optional[str]
    location: Optional[str]
    date: Optional[str]
    time: Optional[str]
    public: Optional[bool]
    user_id: str
    game_id: str

    class Config:
        orm_mode = True
