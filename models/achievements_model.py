from typing import Optional

from models.base_model import BaseModel


class Achievement(BaseModel):
    title: Optional[str]
    rating: Optional[int]
    game_id: str
