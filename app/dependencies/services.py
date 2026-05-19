from fastapi import Depends

from app.modules.auth.auth_service import AuthService
from app.modules.user.user_repository import UserRepository
from app.modules.user.user_service import UserService
from app.dependencies.repositories import get_user_repo

def get_user_service(
    repo: UserRepository =Depends(get_user_repo)
):
    return UserService(repo)

def get_auth_service(repo: UserRepository = Depends(get_user_repo)):
    return AuthService(repo)