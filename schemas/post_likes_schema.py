import datetime
import uuid

from .base_schema import BaseModel


class CreatePostLike(BaseModel):
    post_id: str
    user_id: str


class ReadPostLike(BaseModel):
    id: uuid.UUID
    post_id: str
    user_id: str
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdatePostLike(BaseModel):
    post_id: str
    user_id: str

    class Config:
        orm_mode = True
