from typing import Any
from fastapi import APIRouter

from app.exceptions.app_exception import AppException
from app.modules.user.user_service import UserService
from app.modules.user.user_schema import User, UserCrate

from app.utils.response_utils import (successResponse)

router = APIRouter()
service = UserService()

@router.post('/api/user')
async def create_user(user_data:UserCrate):
    try:
     data :User = service.create_user(user_data)
     return successResponse(data.model_dump(),'user created!',201)
    except AppException as e:
     raise e

@router.get('/api/user')
async def get_all_users():
    data : list[User] = service.get_all_users()
    user_list : list[dict[str ,Any]] = [
        u.model_dump()
        for u in data
        ]
    return successResponse(user_list,'user fetched!') 