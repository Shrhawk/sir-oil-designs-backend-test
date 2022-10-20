from typing import Optional

from models.base_model import BaseModel


class UserAchievement(BaseModel):
    title: Optional[str]
    rating: Optional[str]
    user_id: str
    achievement_id: str
    user_game_id: str
