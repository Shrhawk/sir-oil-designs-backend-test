import datetime

from .base_schema import BaseModel


class CreateAdvertisement(BaseModel):
    post_id: str
    user_id: str


class ReadAdvertisement(BaseModel):
    post_id: str
    user_id: str
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True


class UpdateAdvertisement(BaseModel):
    post_id: str
    user_id: str

    class Config:
        orm_mode = True
