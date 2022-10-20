import time
from typing import Dict

import jwt
from beanie import PydanticObjectId
from fastapi import HTTPException

from config.config import Settings
from models.users_model import User

secret_key = Settings().secret_key


async def token_response(token: str):
    return {"access_token": token}


async def sign_jwt(user_id: str) -> Dict[str, str]:
    """
    Sign jwt token.
    """
    payload = {"user_id": user_id, "expires": time.time() + 2400}
    return await token_response(jwt.encode(payload, secret_key, algorithm="HS256"))


async def decode_jwt(token: str) -> User:
    """
    Decode token to get user.
    """
    decoded_token = jwt.decode(token.encode(), secret_key, algorithms=["HS256"])
    user = await User.find_one(User.id == PydanticObjectId(decoded_token["user_id"]))
    if not user:
        raise HTTPException(
            status_code=403, detail="Invalid user id. Please login again."
        )
    return user
