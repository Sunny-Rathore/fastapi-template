from fastapi import APIRouter, Depends

from app.dependencies.services import get_auth_service
from app.exceptions.app_exception import AppException
from app.modules.auth.auth_schema import LoginRequest
from app.modules.auth.auth_service import AuthService
from app.modules.user.user_schema import UserCrate
from app.utils.response_utils import successResponse

router = APIRouter()

@router.post('/api/login')
async def login(data: LoginRequest, service:AuthService = Depends(get_auth_service)):
    try:
     print(f"Login data : {data.email} {data.password}")
     user = await service.login(data)
     return successResponse(user,'login success')
    except AppException as e:
        raise e

@router.post('/api/register')
async def register(data: UserCrate, service:AuthService = Depends(get_auth_service)):
    try:
     user = await service.register(data)
     return successResponse(user,'user registered')
    except AppException as e:
        raise e