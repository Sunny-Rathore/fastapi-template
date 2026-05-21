from app.exceptions.app_exception import AppException
from app.modules.category.category_model import serialize_categories, serialize_category
from app.modules.category.category_repository import CategoryRepository
from app.modules.category.category_schema import CategoryCreate


class CategoryService:
    def __init__(self,repo:CategoryRepository):
        self.repo = repo
    
    # CREATE    
    async def create(self,data:CategoryCreate)-> dict:
        category = await self.repo.create_category(data.model_dump())
        return serialize_category(category)
    
    # UPDATE
    async def update(self,data:CategoryCreate)-> dict:
        category = await self.repo.create_category(data.model_dump())
        return serialize_category(category)
    
    # FIND ALL         
    async def find_all(self)-> list[dict]:
        categories = await self.repo.find_all()
        return serialize_categories(categories)
    
    # FIND SUB CATEGORY
    async def find_sub_categories(self ,id:str)-> list[dict]:
        categories = await self.repo.find_sub_categories(id)
        return serialize_categories(categories)
    
    # FIND BY ID             
    async def find_by_id(self,id:str)-> dict:
        category = await self.repo.find_by_id(id)
        if not category:
            raise AppException('category not found',404)
        return serialize_category(category)    
    
    # DELETE
    async def delete(self,id:str)-> dict:
        category = await self.repo.delete(id)
        if not category:
            raise AppException('category not found',404)
        return serialize_category(category)      