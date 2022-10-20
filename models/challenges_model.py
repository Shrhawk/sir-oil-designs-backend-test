from datetime import date
from typing import Optional

from models.base_model import BaseModel


class Challenge(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    location: Optional[str]
    date: Optional[date]
    time: Optional[str]
    user_id: str
    game_id: str
