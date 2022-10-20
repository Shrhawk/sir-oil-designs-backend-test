from beanie import PydanticObjectId
from fastapi import HTTPException
from starlette import status

from models import User, Post, UserGame, PostLike, Event


async def get_user_feed(user_id: PydanticObjectId) -> list:
    user = await User.find_one(User.id == user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User Not found")
    post_ids, game_ids, response = [], [], []
    user_games = await UserGame.find(UserGame.user_id == str(user.id)).to_list()
    for user_game in user_games:
        game_ids.append(str(user_game.game_id))
    user_events = await Event.find(
        {
            "$or": [
                {
                    "game_id": {"$in": game_ids}
                },
                {
                    "user_id": str(user.id)
                }
            ]
        }
    ).to_list()
    for user_event in user_events:
        post_ids.append(PydanticObjectId(user_event.post_id))
    user_post_likes = await PostLike.find(PostLike.user_id == str(user.id)).to_list()
    for user_post_like in user_post_likes:
        post_ids.append(PydanticObjectId(user_post_like.post_id))
    get_posts_with_user_loc = await Post.find(
        {
            "loc": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": [user.loc[0], user.loc[1]]
                    },
                    "$maxDistance": 10
                }
            }
        }
    ).to_list()
    for get_posts_with_user_loc_ in get_posts_with_user_loc:
        post_ids.append(get_posts_with_user_loc_.id)
    posts = await Post.find(
        {
            "$or": [
                {
                    "id": {"$in": set(post_ids)},
                },
                {
                    "type": "Event"
                }
            ]
        }
    ).to_list()
    for post in posts:
        user_post = post.dict()
        user_post["details"] = await Event.find_one({"post_id": str(post.id)})
        response.append(user_post)
    return response
