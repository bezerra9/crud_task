from motor.motor_asyncio import AsyncIOMotorClient
from .settings import settings

client = AsyncIOMotorClient(settings.DATABASE_URL)

db = client[settings.DATABASE_NAME]

tasks_collection = db['tasks']