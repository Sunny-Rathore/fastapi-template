from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.dependencies.services import get_product_service
from app.exceptions.app_exception import AppException
from app.modules.product.product_schema import ProductCreate, ProductUpdate
from app.modules.product.product_service import ProductService
from app.utils.response_utils import successResponse

router = APIRouter(
    prefix='/api/product',
    tags = ['Product'],
    dependencies= [Depends(get_current_user)]
)

@router.get('/')
async def find_all(
    search: str  = '',
    page:int = 1,
    limit:int = 10,
    service : ProductService = Depends(get_product_service)
 ):
  try:  
   products = await service.find_all(search ,page ,limit)
   response = {
       'page': page,
       'limit': limit,
       'products': products
   }
   return successResponse(response)
  except AppException as e:
      raise e
  
@router.post('/')
async def add(
    data: ProductCreate,
    service : ProductService = Depends(get_product_service)
 ):
  try:  
   products = await service.create(data.model_dump())
   return successResponse(products)
  except AppException as e:
      raise e      

@router.get('/{id}')
async def get(
    id :str,
    service : ProductService = Depends(get_product_service)
 ):
  try:  
   product = await service.find(id)
   return successResponse(product)
  except AppException as e:
      raise e 

@router.patch('/{id}')
async def patch(
    id :str,
    data: ProductUpdate,
    service : ProductService = Depends(get_product_service)
 ):
  try:  
   product = await service.update(id, data.model_dump())
   return successResponse(product)
  except AppException as e:
      raise e 

@router.delete('/{id}')
async def delete(
    id :str,
    service : ProductService = Depends(get_product_service)
 ):
  try:  
   product = await service.delete(id)
   return successResponse(product)
  except AppException as e:
      raise e   