from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.dependencies.services import get_category_service
from app.exceptions.app_exception import AppException
from app.modules.category.category_schema import CategoryCreate, CategoryUpdate
from app.modules.category.category_service import CategoryService
from app.utils.response_utils import successResponse

router = APIRouter(
    prefix='/api/categories',
    tags=['Categories'],
    dependencies=[Depends(get_current_user)]
) 

# FIND ALL CATEGORY
@router.get('/')
async def find_all( 
    service: CategoryService = Depends(get_category_service)               
    ):
    try:
      categories =  await  service.find_all()
      return successResponse(categories,'category fetched')
    except AppException as e:
       raise e

# ADD CATEGORY   
@router.post('/')
async def create( 
    data : CategoryCreate,            
    service: CategoryService = Depends(get_category_service)               
    ):
    try:
       
      category =  await  service.create(data)
      return successResponse(category,'category created',201)
    except AppException as e:
       raise e
   
# UPDATE CATEGORY  
@router.patch('/{id}')
async def update( 
    id:str,
    data : CategoryUpdate,            
    service: CategoryService = Depends(get_category_service)               
    ):
    try:
      category =  await service.update(id,data)
      return successResponse(category,'category updated')
    except AppException as e:
       raise e 

# DELETE CATEGORY
@router.delete('/{id}')
async def delete( 
    id : str,            
    service: CategoryService = Depends(get_category_service)               
    ):
    try:
      category =  await  service.delete(id)
      return successResponse(category,'category deleted')
    except AppException as e:
       raise e 

# FIND SUB-CATEGORY
@router.get('/{id}/sub')
async def sub_categories( 
    id:str,  
    service: CategoryService = Depends(get_category_service)               
    ):
    try:
      categories =  await  service.find_sub_categories(id)
      return successResponse(categories,'sub-category fetched')
    except AppException as e:
       raise e 
   