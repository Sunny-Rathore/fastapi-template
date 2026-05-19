from app.core.security import create_Jwt_token
from app.exceptions.app_exception import AppException
from app.modules.auth.auth_schema import LoginRequest
from app.modules.user.user_model import serialize_user
from app.modules.user.user_repository import UserRepository
from app.modules.user.user_schema import UserCrate


class AuthService:
    def __init__(self,repo:UserRepository):
        self.repo = repo
    
    # LOGIN
    async def login(self,data: LoginRequest)->dict:
        if '@gmail.com' not in data.email:
            raise AppException('please provide valid email!',400)
        user = await self.repo.find_by_email(data.email)
       
        if not user :
          raise AppException('invalid email',400)
        
        if user['password']!=data.password:
           raise AppException('invalid password',400)
       
        token = create_Jwt_token({'id': str(user['_id'])})
        return {
            'token':token,
            'user':serialize_user(user)
        }
        
    # SIGNUP
    async def register(self,data:UserCrate):
        if "@gmail.com" not in data.email:
            raise AppException('Only gmail accounts are allowed')
        
        user = await  self.repo.find_by_email(data.email)
        if user:
          raise AppException('user already exist',429)
        
        user = await self.repo.create(data.model_dump())
        return serialize_user(user)
    
    # FORGOT PASSWORD
    async def forgot_password(self,email:str):
        pass
    
    # RESET PASSWORD
    async def reset_password(self,password:str,new_password:str):  
        pass 
        