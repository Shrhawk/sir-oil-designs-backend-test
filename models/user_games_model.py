from typing import Optional

from models.base_model import BaseModel


class UserGame(BaseModel):
    status: Optional[str]
    score: Optional[str]
    user_id: str
    game_id: str
