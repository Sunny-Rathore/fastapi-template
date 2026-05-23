from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
class CategoryRepository:
     def __init__(self,collection:AsyncIOMotorCollection):
        self.collection = collection

    # CREATE  
     async def create_category(self,data:dict)-> dict:
        if data.get('parent_id'):
            data['parent_id'] = ObjectId(data['parent_id'])
        result = await self.collection.insert_one(data) 
        data['id'] = result.inserted_id
        return data  
    
    # FIND BY NAME
     async def find_by_name(self,name:str)-> dict|None:
        category = await self.collection.find_one({'name':name})
        if not category:
            return None
        return category
     
    # DELETE 
     async def delete(self,id:str)-> dict|None:
        category = await self.collection.find_one_and_delete({'_id':ObjectId(id)})
        if not category:
            return None
        return category
    
    # UPDATE 
     async def update(self,id:str,data:dict)-> dict|None:
        category = await self.collection.find_one_and_update({'_id':ObjectId(id)},{'$set':data},return_document=True)
        if not category:
            return None
        return category
     
     # Find All
     async def find_all(self)-> list[dict]:
        cursor = self.collection.find({'parent_id':None}) 
        category = await cursor.to_list(length=None)
        return category
     
     # FIND SUB-CATEGORY
     async def find_sub_categories(self,id:str)-> list[dict]:
        cursor = self.collection.find({'parent_id': ObjectId(id)}) 
        category = await cursor.to_list(length=None)
        return category