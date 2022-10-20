import uuid
from typing import Optional, List
from typing import Union

from fastapi.security import HTTPBasicCredentials
from pydantic import EmailStr, root_validator

from models import Challenge, Post, UserGame, UserAchievement, Event, Advertisement, PostLike
from .base_schema import BaseModel


class UserSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {"example": {"username": "string", "password": "string"}}


class UserData(BaseModel):
    username: str
    email: EmailStr
    password: str
    bio: Optional[str]
    loc: Optional[List[float]]


class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    username: str
    bio: Optional[str]
    loc: List[float]

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    user_id: Union[uuid.UUID, None] = None


class PostAndLikes(Post):
    post_likes: List[PostLike]


class EventPost(PostAndLikes):
    event: Event


class AdvertisementPost(PostAndLikes):
    advertisement: Advertisement


class UserDetails(UserSignUp):
    challenges: List[Challenge]
    posts: List[Union[EventPost, AdvertisementPost]]
    user_games: List[UserGame]
    user_achievements: List[UserAchievement]

    class Config:
        orm_mode = True
