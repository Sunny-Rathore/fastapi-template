from typing import Any, Self
from unittest import result

from bson import ObjectId

from app.modules.user.user_schema import User, UserCrate
from motor.motor_asyncio import AsyncIOMotorCollection

from app.modules.user.user_serializer import serialize_user, serialize_users

class UserRepository:
    def __init__(self,collection:AsyncIOMotorCollection):
        self.collection = collection
     
    #CREATE USER 
    async def create(self,user_data : dict) -> dict :
        result = await  self.collection.insert_one(user_data)
        user = user_data.copy()
        user['id'] = str(result.inserted_id)
        return serialize_user(user)
      
    # FIND ALL USERS
    async def find_all(self)-> list[dict] :
      users_cursor = self.collection.find()
      users = await users_cursor.to_list(length=None)
      return serialize_users(users)
    
    # FIND USER BY ID    
    async def find_by_id(self,id:str)-> dict | None:    
       user = await self.collection.find_one({
            '_id': ObjectId(id)
        })
       
       if not user:
           return None
       
       return serialize_user(user)
    
    #FIND BY EMAIL
    async def find_by_email(self ,email:str)-> dict| None:
        user = await self.collection.find_one({'email':email})
        if not user:
           return None
        return serialize_user(user)
    
    #DELETE USER
    async def delete(self,id:str)-> str| None:
        await self.collection.delete_one({'_id':ObjectId(id)})
        return id
    
    #UPDATE USER
    async def update(self,id:str, data:dict)-> dict:
     updated_user = await self.collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": data},
        return_document=True
    )
     return serialize_user(updated_user)