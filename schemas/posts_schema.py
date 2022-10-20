import datetime
from typing import Optional, Union, List

from .advertisements_schema import ReadAdvertisement
from .base_schema import BaseModel
from .events_schema import ReadEvent


class CreatePost(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    loc: Optional[List[float]]
    user_id: str
    total_likes: Optional[int]


class ReadPost(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    loc: Optional[List[float]]
    user_id: str
    total_likes: Optional[int]
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdatePost(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    loc: Optional[List[float]]
    user_id: str
    total_likes: Optional[int]

    class Config:
        orm_mode = True


class UserPost(ReadPost):
    details: Union[ReadEvent, ReadAdvertisement]
