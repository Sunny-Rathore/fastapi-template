def serialize_category(category:dict)->dict:
    return {
        'id': str(category['_id']),
        'parent_id': str(category['parent_id']) if category['parent_id'] else None,
        'name': category['name'],
        'slug': category['slug'],
        'image': str(category['image']) if category['image'] else None,
        'is_active' :category['is_active'],
    }
    
def   serialize_categories(categories:list[dict])-> list[dict]:
      return [serialize_category(category) for category in categories] 