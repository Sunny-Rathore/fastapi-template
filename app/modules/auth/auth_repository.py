
from app.modules.auth.auth_schema import LoginResponse
from app.modules.user.user_schema import User


class AuthRepository:
   def login(self,email:str,password:str)->LoginResponse:
        
        return LoginResponse(token='')