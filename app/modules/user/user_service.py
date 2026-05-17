from app.exceptions.app_exception import AppException
from app.modules.user.user_repository import UserRepository
from app.modules.user.user_schema import UserCrate

class UserService():
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self,user_data:UserCrate):
        if "@gmail.com" not in user_data.email:
            raise AppException('only gmail account allowed')
        return  self.repository.create_user(user_data.model_dump())

    def get_all_users(self):
        return self.repository.get_all_users()    