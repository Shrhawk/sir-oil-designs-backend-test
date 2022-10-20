from models import (
    User, Game, Achievement,
    Advertisement, Post, Challenge,
    Event, PostLike, UserGame, UserAchievement
)
from routes.user import hash_helper


async def initiate_db():
    new_user = await User(**{
        "first_name": "string",
        "last_name": "string",
        "username": "string1",
        "email": "user1@example.com",
        "password": hash_helper.encrypt("string1"),
        "bio": "string",
        "loc": [31.5204, 74.3587]
    }).create()
    new_user2 = await User(**{
        "first_name": "string2",
        "last_name": "string2",
        "username": "string2",
        "email": "user2@example.com",
        "password": hash_helper.encrypt("string2"),
        "bio": "string 2",
        "loc": [32.4945, 74.5229]
    }).create()
    game = await Game(**{
        "title": "cricket",
        "description": "something",
        "meta_data": {}
    }).create()
    achievement = await Achievement(**{
        "title": "Achievement",
        "rating": 5,
        "game_id": str(game.id)
    }).create()
    post = await Post(**{
        "title": "First Post",
        "description": "Post description",
        "status": "Active",
        "type": "Event",
        "loc": [31.5204, 74.3587],
        "user_id": str(new_user.id),
        "total_likes": 1
    }).create()
    post2 = await Post(**{
        "title": "First Post",
        "description": "Post description",
        "status": "Active",
        "type": "Advertisement",
        "loc": [31.5204, 74.3587],
        "user_id": str(new_user.id),
        "total_likes": 1
    }).create()
    post3 = await Post(**{
        "title": "First Post 2",
        "description": "Post description",
        "status": "Active",
        "type": "Event",
        "loc": [32.4945, 74.5229],
        "user_id": str(new_user2.id),
        "total_likes": 2
    }).create()
    post4 = await Post(**{
        "title": "First Post 2",
        "description": "Post description",
        "status": "Active",
        "type": "Advertisement",
        "loc": [32.4945, 74.5229],
        "user_id": str(new_user2.id),
        "total_likes": 2
    }).create()
    advertisement = await Advertisement(**{
        "meta_data": {"data": 0},
        "post_id": str(post2.id),
        "user_id": str(new_user.id)
    }).create()
    advertisement2 = await Advertisement(**{
        "meta_data": {"data": 0},
        "post_id": str(post4.id),
        "user_id": str(new_user2.id)
    }).create()
    challenge = await Challenge(**{
        "title": "First Challenge",
        "description": "Challenge description",
        "status": "Active",
        "location": "location",
        "date": None,
        "time": None,
        "user_id": str(new_user.id),
        "game_id": str(game.id)
    }).create()
    event = await Event(**{
        "title": "First Challenge",
        "description": "Challenge description",
        "status": "Active",
        "location": "location",
        "public": True,
        "date": None,
        "time": None,
        "post_id": str(post.id),
        "user_id": str(new_user.id),
        "game_id": str(game.id)
    }).create()
    event2 = await Event(**{
        "title": "First Challenge",
        "description": "Challenge description",
        "status": "Active",
        "location": "location",
        "public": True,
        "date": None,
        "time": None,
        "post_id": str(post3.id),
        "user_id": str(new_user2.id),
        "game_id": str(game.id)
    }).create()
    post_like = await PostLike(**{
        "post_id": str(post.id),
        "user_id": str(new_user.id)
    }).create()
    post_like2 = await PostLike(**{
        "post_id": str(post3.id),
        "user_id": str(new_user2.id)
    }).create()
    post_like3 = await PostLike(**{
        "post_id": str(post3.id),
        "user_id": str(new_user.id)
    }).create()
    user_game = await UserGame(**{
        "status": "Active",
        "score": 10,
        "game_id": str(game.id),
        "user_id": str(new_user.id)
    }).create()
    user_achievement = await UserAchievement(**{
        "title": "test",
        "rating": 5,
        "user_id": str(new_user.id),
        "achievement_id": str(achievement.id),
        "user_game_id": str(user_game.id)
    }).create()
    return True
