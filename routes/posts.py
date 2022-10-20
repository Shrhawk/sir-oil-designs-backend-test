from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from auth.jwt_bearer import get_current_user
from crud.post import get_user_feed
from models.users_model import User
from schemas.posts_schema import UserPost

router = APIRouter()


@router.post("/user_feed", response_model=List[UserPost])
async def user_feed(user: User = Depends(get_current_user)) -> List[UserPost]:
    """
    User feed route.
    """
    post_details = await get_user_feed(user_id=PydanticObjectId(user.id))
    if not post_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Posts not found")
    return post_details
