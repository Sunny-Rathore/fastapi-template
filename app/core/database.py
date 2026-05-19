from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import settings
import certifi

client = AsyncIOMotorClient(settings.MONGO_URI,tlsCAFile=certifi.where())
db = client[settings.DATABASE_NAME ]
user = db['users']
 