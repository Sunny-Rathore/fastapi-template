from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.dependencies.services import get_address_service
from app.exceptions.app_exception import AppException
from app.modules.address.address_schema import AddressCreate, AddressUpdate
from app.modules.address.address_service import AddressService
from app.utils.response_utils import successResponse

router = APIRouter(
    prefix='/api/address',tags=['Address'],
    dependencies=[Depends(get_current_user)]
    )

# Get
@router.get('/')
async def get_address(
    current_user = Depends(get_current_user),
    service: AddressService =Depends(get_address_service)
):
    try:
     address = await service.find_all_address(current_user['id'])
     return successResponse(address,'address fetched')
    except AppException as e:
       raise e

@router.post('/')   
async def create_address(
    address_data : AddressCreate,
    current_user = Depends(get_current_user),
    service: AddressService =Depends(get_address_service),
    
):
    try:
       address_data.user_id =  current_user['id']
       address = await service.create_address(address_data)
       return successResponse(address,'address created!',201)
    except AppException as e:
       raise e   
    
@router.patch('/{id}') 
async def update_address(
    id:str,
    address_data : AddressUpdate,
    service: AddressService =Depends(get_address_service),
    
):
    try:
       address = await service.update_address(id, address_data)
       return successResponse(address,'address updated')
    except AppException as e:
       raise e     
    
@router.delete('/{id}') 
async def delete_address(
    id:str,
    service: AddressService =Depends(get_address_service),
    
):
    try:
       address = await service.delete_address(id)
       return successResponse(address,'address deleted')
    except AppException as e:
       raise e   
