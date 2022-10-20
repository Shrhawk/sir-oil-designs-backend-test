from typing import Optional, Literal

import pymongo
from beanie import Indexed

from models.base_model import BaseModel


class Post(BaseModel):
    title: Optional[str]
    status: Optional[str]
    loc: Indexed(list, index_type=pymongo.GEOSPHERE)
    type: Literal["Event", "Advertisement"]
    user_id: str
    total_likes: Optional[int]

    class Settings:
        indexes = [
            [("loc", pymongo.GEOSPHERE)],  # GEO index
        ]
