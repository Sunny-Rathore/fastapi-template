from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import settings
 
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME ]
user = db['users']
address = db['address']
category =db['category']
product =db['product']

 