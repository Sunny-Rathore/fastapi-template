def serialize_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "name": user["name"],
        "address": user["address"]
    }


def serialize_users(users) -> list:
    return [serialize_user(user) for user in users]