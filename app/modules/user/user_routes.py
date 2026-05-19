from typing import Any
from fastapi import APIRouter, Depends

from app.dependencies import services
from app.exceptions.app_exception import AppException
from app.modules.user.user_service import UserService
from app.modules.user.user_schema import UserCrate,UserUpdate
from app.dependencies.services import get_user_service
from app.utils.response_utils import (successResponse)

router = APIRouter()
 

# CREATE
@router.post('/api/user')
async def create_user(user_data:UserCrate ,service :UserService = Depends(get_user_service)):
    try:
     data = await service.create(user_data)
     print(f"Route Return Data {data}")
     return successResponse(data,'user created!',201)
    except AppException as e:
     raise e

# GET ALL
@router.get('/api/user')
async def get_all_users(service :UserService = Depends(get_user_service)):
    try:
      data  = await service.find_all()
      return successResponse(data,'user list fetched!') 
    except AppException as e:
     raise e

# GET BY ID
@router.get('/api/user/{id}')
async def get_user_by_id(id:str ,service :UserService = Depends(get_user_service)):
    try: 
      user = await service.find_by_id(id)
      return successResponse(user,'user fetched!') 
    except AppException as e:
     raise e

# UPDATE
@router.patch('/api/user/{id}')
async def update_user(id:str, user: UserUpdate ,service :UserService = Depends(get_user_service)):
    try: 
      updatedUser = await service.update(id,user)
      return successResponse(updatedUser,'user updated!') 
    except AppException as e:
     raise e
 
# DELETE
@router.delete('/api/user/{id}')
async def delete_user(id:str ,service : UserService = Depends(get_user_service)):
    try: 
      user = await service.delete(id)
      return successResponse(user,'user deleted!') 
    except AppException as e:
     raise e