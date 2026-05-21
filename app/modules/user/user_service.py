 

from app.exceptions.app_exception import AppException
from app.modules.user.user_model import serialize_user, serialize_users
from app.modules.user.user_repository import UserRepository
from app.modules.user.user_schema import UserCrate,UserUpdate

class UserService():
    def __init__(self,repo : UserRepository):
        self.repo = repo
    
    # CREATE USER 
    async def create(self,data : UserCrate)-> dict:
        if "@gmail.com" not in data.email:
            raise AppException('Only gmail accounts are allowed')
        
        user = await  self.repo.find_by_email(data.email)
        if user:
          raise AppException('user already exist',429)
        
        user = await self.repo.create(data.model_dump())
        return serialize_user(user)
    
    # FIND ALL USERS
    async def find_all(self):
      users= await self.repo.find_all() 
      return serialize_users(users)     
    
    # FIND USER BY ID    
    async def find_by_id(self,id:str)-> dict:
        user = await  self.repo.find_by_id(id)
        if not user :
          raise AppException('user not found',400)
        return serialize_user(user) 
    
    # UPDATE USER
    async def update(self,id:str,data:UserUpdate)-> dict:
        user = await self.repo.update(id ,data.model_dump())
        if not user :
          raise AppException('user not found',400)
        return serialize_user(user)
    
    # DELETE USER
    async def delete(self,id:str)-> dict:
        deleted_user: dict | None = await self.repo.delete(id)
        if not deleted_user:
          raise AppException('user not found',400)
        return serialize_user(deleted_user) 