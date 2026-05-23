from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.exceptions.app_exception import AppException
from app.modules.user.user_service import UserService
from app.modules.user.user_schema import UserCrate,UserUpdate
from app.dependencies.services import get_user_service
from app.utils.response_utils import (successResponse)

router = APIRouter(
  prefix='/api/user',
  tags=['Users'],
  dependencies = [Depends(get_current_user)]
)
 

# CREATE
@router.post('/')
async def create_user(user_data: UserCrate ,service :UserService = Depends(get_user_service)):
    try:
     data = await service.create(user_data)
     return successResponse(data,'user created!',201)
    except AppException as e:
     raise e

# GET ALL
@router.get('/')
async def get_all_users(
  search: str  = '',
  page: int  = 1,
  limit : int = 10,
  service :UserService = Depends(get_user_service)
  ):
    try:
      data  = await service.find_all(search ,page ,limit)
      response = {
        'page': page,
        'limit': limit,
        'users': data
      }
      return successResponse(response,'user list fetched!') 
    except AppException as e:
     raise e

# FIND ME
@router.get('/me')
async def find_me(
  current_user = Depends(get_current_user), service : UserService = Depends(get_user_service)):
    try: 
      user = await service.find_by_id(current_user['id'])
      return successResponse(user,'user fetched!') 
    except AppException as e:
     raise e
    
# GET BY ID
@router.get('/{id}')
async def get_user_by_id(
  id:str, service :UserService = Depends(get_user_service)):
    try: 
      user = await service.find_by_id(id)
      return successResponse(user,'user fetched!') 
    except AppException as e:
     raise e

# UPDATE
@router.patch('/{id}')
async def update_user(id:str, user: UserUpdate ,service :UserService = Depends(get_user_service)):
    try: 
      updatedUser = await service.update(id,user)
      return successResponse(updatedUser,'user updated!') 
    except AppException as e:
     raise e
 
# DELETE
@router.delete('/{id}')
async def delete_user(id:str ,service : UserService = Depends(get_user_service)):
    try: 
      user = await service.delete(id)
      return successResponse(user,'user deleted!') 
    except AppException as e:
     raise e