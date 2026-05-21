
from bson import ObjectId
from motor.motor_asyncio import  AsyncIOMotorCollection

class AddressRepository:
    def __init__(self ,collection:AsyncIOMotorCollection):
        self.collection = collection
   
   # CREATE ADDRESS
    async def create_address(self,data:dict)-> dict:
      data['user_id'] = ObjectId(data['user_id'])
      result = await self.collection.insert_one(data)
      data['id'] = result.inserted_id
      return data
   
   # FIND ADDRESS BY ID
    async def find_address(self,id:str)-> dict|None:
      address = await self.collection.find_one({'_id': ObjectId(id)}) 
      if not address:
        return None
      return address
    
    # FIND ADDRESS List
    async def find_all_address(self,user_id:str)-> list[dict]:
      address_doc = self.collection.find({'user_id':  ObjectId(user_id)}) 
      return await address_doc.to_list(length=None)

   # UPDATE ADDRESS
    async def update_address(self,id:str,data:dict)-> dict|None:
      address =  await self.collection.find_one_and_update(
          {'_id':ObjectId(id)},
          {'$set': data},
          return_document=True
       )
      if not address:
        return None
      return address
         
   # DELETE ADDRESS 
    async def deleteAddress(self,id:str)-> dict|None:
      result = await self.collection.find_one_and_delete({'_id':ObjectId(id)})
      if not result :
        return None
      return result
