from app.exceptions.app_exception import AppException
from app.modules.product.product_repository import ProductRepository
from app.modules.product.product_serialize import serialize_product


class ProductService:
    def __init__(self,repo:ProductRepository):
        self.repo = repo
        
    # CREATE 
    async def create(self,data:dict)-> dict:
        result = await self.repo.create(data)
        return serialize_product(result)
    
    # FIND ALL
    async def find_all(self,search : str, page:int,limit:int)-> list[dict]:
        products = await self.repo.find_all(search,page ,limit)
        return [serialize_product(product) for  product in products ]
        
    # FIND 
    async def find(self,id:str)-> dict|None:
      product = await self.repo.find(id)
      if not product:
          raise AppException('product not found',404)
      return serialize_product(product)
    
    # UPDATE
    async def update(self,id:str,data:dict)-> dict|None:
        product = await self.repo.update(id,data)
        if not product:
            raise AppException('product not found',404)
        return serialize_product(product)
    
    # DELETE
    async def delete(self,id:str)-> dict|None:
        product = await self.repo.delete(id)
        if not product:
            raise AppException('product not found',404)
        return serialize_product(product)