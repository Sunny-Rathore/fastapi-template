from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection

class UserRepository:
    def __init__(self,collection:AsyncIOMotorCollection):
        self.collection = collection
     
    # CREATE USER 
    async def create(self,user_data : dict) -> dict :
        result = await self.collection.insert_one(user_data)
        user = user_data.copy()
        user['id'] =result.inserted_id
        return user
      
    # FIND ALL USERS
    async def find_all(self,search:str , page:int, limit:int,
        )-> list[dict] :
        quey = {
          '$or':[
            {"name":{"$regex":search,"$options":'i'}},
            {'email':{"$regex":search,'$options':'i'}}
               
          ]
        }  
        users_cursor = self.collection.find(quey).skip((page-1)*limit).limit(limit)
        users = await users_cursor.to_list()
        return users
    
    # FIND USER BY ID    
    async def find_by_id(self,id:str)-> dict | None:    
        user = await self.collection.find_one({
            '_id': ObjectId(id)
        })
       
        if not user:
           return None
       
        return user
    
    # FIND BY EMAIL
    async def find_by_email(self ,email:str)-> dict| None:
        user = await self.collection.find_one({'email':email})
        if not user:
           return None
        return user
    
    # DELETE USER
    async def delete(self,id:str)-> dict|None:
        result =  await self.collection.find_one_and_delete({'_id': ObjectId(id)})
        if not result:
           return None
        return result
    
    # UPDATE USER
    async def update(self,id:str, data:dict)-> dict:
     updated_user = await self.collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": data},
        return_document=True
    )
     return updated_user