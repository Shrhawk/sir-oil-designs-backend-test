import pymongo
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import settings
from models import *


async def initiate_database():
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(),
        document_models=[
            User, UserGame, UserAchievement,
            Post, PostLike, Game, Event,
            Challenge, Advertisement, Achievement,
        ]
    )
    # to create indexes on collection
    db = client.get_default_database()
    db.get_collection("Post").create_index([("loc", pymongo.GEOSPHERE)])
    db.get_collection("User").create_index([("loc", pymongo.GEOSPHERE)])
