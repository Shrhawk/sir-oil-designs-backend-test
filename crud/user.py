from beanie import PydanticObjectId
from fastapi import HTTPException
from starlette import status

from models import User, Challenge, Post, UserGame, UserAchievement, Event, Advertisement, PostLike


async def get_user_detail(user_id: PydanticObjectId) -> dict:
    """
    Get a user detail.
    """
    user = await User.find_one(User.id == user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User Not found")
    user_details = user.dict()
    user_details["challenges"] = await Challenge.find(Challenge.user_id == str(user.id)).to_list()
    user_details["posts"] = await Post.find(Post.user_id == str(user.id)).to_list()
    for post_index, user_post in enumerate(user_details["posts"]):
        user_details["posts"][post_index] = user_details["posts"][post_index].dict()
        if user_post.type == "Event":
            event = await Event.find_one(Event.post_id == str(user_post.id))
            user_details["posts"][post_index]["event"] = event
        else:
            advertisement = await Advertisement.find_one(Advertisement.post_id == str(user_post.id))
            user_details["posts"][post_index]["advertisement"] = advertisement
        user_details["posts"][post_index]["post_likes"] = await PostLike.find(
            PostLike.post_id == str(user_post.id)
        ).to_list()
    user_details["user_games"] = await UserGame.find(UserGame.user_id == str(user.id)).to_list()
    user_details["user_achievements"] = await UserAchievement.find(UserAchievement.user_id == str(user.id)).to_list()
    return user_details
