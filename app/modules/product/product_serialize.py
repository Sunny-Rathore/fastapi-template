from bson import ObjectId

from app.modules.product.product_schema import ProductCreate


def serialize_product(data:dict):
   data['id'] = str(data['_id'])
   data['category_id'] = str(data['category_id'])
   product: ProductCreate = ProductCreate.model_validate(data)
   serialized = product.dict()
   return serialized
    