from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ProductImage(BaseModel):
    url:str
    alt_text: Optional[str] = None

class VariantAttribute(BaseModel):
    name: str
    value: str
    
    
class ProductVariant(BaseModel):
    sku: str
    attributes: List[VariantAttribute]
    price: float
    compare_price: Optional[float] = None
    stock: int
    image: Optional[str] = None
    weight: Optional[float] = None
    is_active: bool = True
    
 
    
class ProductCreate(BaseModel):
    id: Optional[str] = None
    title: str
    slug: str
    description: str
    brand: Optional[str] = None
    category_id: str
    tags: List[str] = []
    images: List[ProductImage] = []
    variants: List[ProductVariant]
    rating_average: float = 0
    rating_count: int = 0
    is_published: bool = True
    created_by: str
    # created_at: datetime = datetime.utcnow()
    # updated_at: datetime = datetime.utcnow()
    

class ProductUpdate(BaseModel):
    title: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    brand: Optional[str] 
    category_id: Optional[str]
    tags: List[str]  
    images: List[ProductImage]  
    variants: List[ProductVariant]
    rating_average: float  
    rating_count: Optional[int]  
    is_published: Optional[bool] 
    # updated_at: datetime = datetime.utcnow()    