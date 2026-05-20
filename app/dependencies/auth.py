from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.security import verify_token
from app.dependencies.services import get_user_service
from app.exceptions.app_exception import AppException
from app.modules.user.user_service import UserService

security = HTTPBearer()
async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        service: UserService = Depends(get_user_service)
):
  token = credentials.credentials
  
  if not token :
    raise AppException('token missing',401)
  payload = verify_token(token)
  
  if not payload:
    raise AppException('invalid token',401)
  user = await service.find_by_id(payload.get('id',''))
  
  if not user:
    raise AppException('user not found',404)
  return user
