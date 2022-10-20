import datetime
import uuid
from typing import Optional

from .base_schema import BaseModel


class CreateGame(BaseModel):
    title: str
    description: Optional[str]
    meta_data: dict


class ReadGame(BaseModel):
    id: uuid.UUID
    title: str
    description: Optional[str]
    meta_data: dict
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdateGame(BaseModel):
    title: str
    description: Optional[str]
    meta_data: dict

    class Config:
        orm_mode = True
