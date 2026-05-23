from typing import Optional

from pydantic import BaseModel

class CategoryCreate(BaseModel):
      name:str
      slug:str
      parent_id: Optional[str] = None
      image: Optional[str]= None
      is_active: Optional[bool] = True
      
class CategoryUpdate(BaseModel):
      name: Optional[str]= None
      slug:Optional[str]=None
      parent_id: Optional[str] = None
      image: Optional[str]= None
      is_active: Optional[bool] = True      


      