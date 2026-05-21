from app.modules.address.address_repository import AddressRepository
from app.modules.user.user_repository import UserRepository
from app.core.database import db

def get_user_repo():
    return UserRepository(db.user)

def get_address_repo():
    return AddressRepository(db.address)