from pydantic import BaseModel, Field

# class Address(BaseModel):
#      id :str
#      user_id:str
#      street:str
#      city:str
#      country:str

class AddressCreate(BaseModel):
    user_id: str | None = Field(default=None)
    street:str
    city:str
    country:str

class AddressUpdate(BaseModel):
    street:str
    city:str
    country:str       
