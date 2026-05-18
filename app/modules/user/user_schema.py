from pydantic import BaseModel

class User(BaseModel):
      id:int
      email:str
      name:str
      address:str

class UserCrate(BaseModel):
      email:str
      name:str
      address:str

class UserUpdate(BaseModel):
      name:str
      address:str