from typing import Optional

import pymongo
from beanie import Indexed

from models.base_model import BaseModel


class User(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    bio: Optional[str]
    loc: Indexed(list, index_type=pymongo.GEOSPHERE)

    class Settings:
        indexes = [
            [("loc", pymongo.GEOSPHERE)],  # GEO index
        ]
