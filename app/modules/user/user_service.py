import re

from app.exceptions.app_exception import AppException
from app.modules.user.user_repository import UserRepository
from app.modules.user.user_schema import UserCrate,UserUpdate

class UserService():
    def __init__(self,repo:UserRepository):
        self.repo = repo

    async def create(self,user_data:UserCrate)-> dict:
        if "@gmail.com" not in user_data.email:
            raise AppException('Only gmail accounts are allowed')
        
        user = await  self.repo.find_by_email(user_data.email)
        if user:
          raise AppException('user already exist',429)
        
        return await self.repo.create(user_data.model_dump())

    async def find_all(self):
        return await self.repo.find_all()    
    
    async def delete(self,id:str)-> dict:
        user = await  self.repo.find_by_id(id)
        if not user :
          raise AppException('user not found',400)
        await self.repo.delete(id)
        return user
    
    async def find_by_id(self,id:str)-> dict:
        user = await  self.repo.find_by_id(id)
        if not user :
          raise AppException('user not found',400)
        return user
    
    async def update(self,id:str,data:UserUpdate)-> dict:
        user = await  self.repo.find_by_id(id)
        if not user :
          raise AppException('user not found',400)
        user = await self.repo.update(id ,data.model_dump())
        if not user :
          raise AppException('user not found',400)
        return user