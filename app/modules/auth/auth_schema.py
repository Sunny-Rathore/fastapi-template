from pydantic import BaseModel

from app.modules.user.user_schema import User

class LoginRequest(BaseModel):
    email:str
    password:str
 