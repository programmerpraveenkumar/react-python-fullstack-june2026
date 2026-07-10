from pydantic import BaseModel
from typing import Optional
"""
    email,
    name
    mobile,
    password,
    dob
    address
"""

class Register(BaseModel):
    email:str
    name:str
    mobile:int
    password:str
    dob:str
    # this address is optional for request body
    address:Optional[str] = None

class User_Update(BaseModel):
    id:int
    name:str
    

class Login(BaseModel):
	email:str
	password:str


class AddCart(BaseModel):
      name:str
      qty:int
      price:float