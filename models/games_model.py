from typing import Optional

from models.base_model import BaseModel


class Game(BaseModel):
    title: str
    description: Optional[str]
    meta_data: dict
