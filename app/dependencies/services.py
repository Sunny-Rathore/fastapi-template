from fastapi import Depends

from app.modules.address.address_repository import AddressRepository
from app.modules.address.address_service import AddressService
from app.modules.auth.auth_service import AuthService
from app.modules.category.category_repository import CategoryRepository
from app.modules.category.category_service import CategoryService
from app.modules.product.product_repository import ProductRepository
from app.modules.product.product_service import ProductService
from app.modules.user.user_repository import UserRepository
from app.modules.user.user_service import UserService
from app.dependencies.repositories import get_address_repo, get_category_repo, get_product_repo, get_user_repo

def get_user_service(
    repo: UserRepository =Depends(get_user_repo)
):
    return UserService(repo)

def get_auth_service(repo: UserRepository = Depends(get_user_repo)):
    return AuthService(repo)

def get_address_service(repo: AddressRepository = Depends(get_address_repo)):
    return AddressService(repo)

def get_category_service(repo: CategoryRepository = Depends(get_category_repo)):
    return CategoryService(repo)

def get_product_service(repo: ProductRepository = Depends(get_product_repo)):
    return ProductService(repo)