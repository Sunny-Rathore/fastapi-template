

def serialize_address(address):
     return {
        'id': str(address['_id']),
        'user_id': str(address['user_id']),
        'street': address['street'],
        'city': address['city'],
        'country': address['country']
     }


def serialize_address_list(addressList):
     return [serialize_address(address) for address in addressList ]