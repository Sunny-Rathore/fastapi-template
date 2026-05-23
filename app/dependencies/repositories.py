from app.modules.address.address_repository import AddressRepository
from app.modules.category.category_repository import CategoryRepository
from app.modules.product.product_repository import ProductRepository
from app.modules.user.user_repository import UserRepository
from app.core.database import db

def get_user_repo():
    return UserRepository(db.user)

def get_address_repo():
    return AddressRepository(db.address)

def get_category_repo():
    return CategoryRepository(db.category)

def get_product_repo():
    return ProductRepository(db.product)