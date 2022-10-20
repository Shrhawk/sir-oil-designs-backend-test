from typing import Optional

from models.base_model import BaseModel


class Event(BaseModel):
    title: Optional[str]
    description: Optional[str]
    location: Optional[str]
    date: Optional[str]
    time: Optional[str]
    public: Optional[bool]
    user_id: str
    post_id: str
    game_id: str
