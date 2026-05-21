from app.exceptions.app_exception import AppException
from app.modules.address.address_model import serialize_address, serialize_address_list
from app.modules.address.address_repository import AddressRepository
from app.modules.address.address_schema import AddressCreate, AddressUpdate
from app.utils.response_utils import successResponse


class AddressService:
    def __init__(self,repo:AddressRepository):
        self.repo = repo

    # CREATE
    async def create_address(self,data:AddressCreate):
      address = await self.repo.create_address(data.model_dump())
      return serialize_address(address)
    
    # FIND BY ID
    async def find_address(self,id:str)-> dict:
       address = await self.repo.find_address(id)
       if not address:
          raise AppException('address not found',404)
      
       return serialize_address(address)
    
    async def find_all_address(self,id:str)-> list[dict]:
       address = await self.repo.find_all_address(id) 
       return serialize_address_list(address)
    
    # UPDATE
    async def update_address(self,id:str,data:AddressUpdate):
      updated_address = await self.repo.update_address(id,data.model_dump()) 
      if not updated_address:
         raise AppException('address not found' ,404)  
      return serialize_address(updated_address)
    
    # DELETE
    async def delete_address(self,id:str)-> dict:
      deleted_address = await self.repo.deleteAddress(id)
      if not deleted_address:
          raise AppException('address not found',404)
      
      return serialize_address(deleted_address)

