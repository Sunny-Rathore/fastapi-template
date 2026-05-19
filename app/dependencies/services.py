from fastapi import Depends

from app.modules.user.user_repository import UserRepository
from app.modules.user.user_service import UserService
from app.dependencies.repositories import get_user_repo

def get_user_service(
    repo: UserRepository =Depends(get_user_repo)
):
    return UserService(repo)