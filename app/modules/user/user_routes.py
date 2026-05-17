from fastapi import APIRouter
from app.exceptions.app_exception import AppException
from app.modules.user.user_service import UserService
from app.modules.user.user_schema import UserCrate
from app.utils.response_utils import (successResponse ,errorResponse)

router = APIRouter()
service = UserService()

@router.post('/api/user')
async def create_user(user_data:UserCrate):
    try:
     data = service.create_user(user_data)
     return successResponse(data,'user created!',201)
    except AppException as e:
     raise e

@router.get('/api/user')
async def get_all_users():
    data = service.get_all_users()
    return successResponse(data,'user fetched!') 