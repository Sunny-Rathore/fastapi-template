from typing import Any

from app.modules.user.user_schema import User, UserCrate


class UserRepository:
    def __init__(self):
        self.users : list[dict[str, Any]] = []
     
    #create user 
    def create_user(self,user_data : UserCrate) -> User:
        user: dict[str, object] = {  
              "id" : len(self.users)+1,
              "name" : user_data.name,
              "email" : user_data.email,
              "address" : user_data.address
            } 
           
        self.users.append(user)
        return User(
            id = len(self.users)+1,
            name = user_data.name,
            email =  user_data.email,
            address = user_data.address
        )
      
    # get all user
    def get_all_users(self) -> list[User]:
        return [
            User(
                id = u["id"],
                name = u["name"],
                email = u["email"],
                address = u["address"]
            )
            for u in self.users 
            ]