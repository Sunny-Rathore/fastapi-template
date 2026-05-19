from app.modules.user.user_repository import UserRepository
from app.core.database import db

def get_user_repo():
    return UserRepository(db.user)