from pydantic import BaseModel

class UserCrate(BaseModel):
      email:str
      name:str
      address:str

class UserUpdate(BaseModel):
       name:str
       address:str