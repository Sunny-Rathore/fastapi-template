from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.exceptions.app_exception import AppException
from app.modules.category.category_service import CategoryService

router = APIRouter(
    prefix='/api/categories',
    tags=['Categories'],
    dependencies=[Depends(get_current_user)]
) 

@router.get('/')
async def find_all( 
    service: CategoryService = Depends()               
                   ):
    try:
        pass
    except AppException as e:
       raise e