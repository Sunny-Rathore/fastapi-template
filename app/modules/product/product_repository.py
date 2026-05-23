from bson import ObjectId
from motor.motor_asyncio import  AsyncIOMotorCollection

from app.modules.product.product_schema import ProductCreate
class ProductRepository:
    def __init__(self,collection:AsyncIOMotorCollection):
        self.collection = collection
        
    # CREATE 
    async def create(self,data:dict)-> dict:
        data['category_id'] = ObjectId(data['category_id'])
        result = await self.collection.insert_one(data)
        data['id'] = str(result.inserted_id)
        return data
    
    # FIND ALL
    async def find_all(self,search :str, page:int, limit:int)-> list[dict]:
        query = {"title": {"$regex": search, "$options":'i'}}
        cursor = self.collection.find(query).skip((page-1)*limit).limit(limit)
        return await cursor.to_list(length=None)
        
    # FIND 
    async def find(self,id:str)-> dict|None:
      product = await self.collection.find_one({'_id':ObjectId(id)})
      if not product:
          return None
      return product
    
    # UPDATE
    async def update(self,id:str,data:dict)-> dict|None:
        product = await self.collection.find_one_and_update({
            '_id':ObjectId(id),},
            {'$set':data},
            return_document=True
            )
        if not product:
            return None
        return product
    
    # DELETE
    async def delete(self,id:str)-> dict|None:
        product = await self.collection.find_one_and_delete({'_id':ObjectId(id)})
        if not product:
            return None
        return product
        
    
    

 