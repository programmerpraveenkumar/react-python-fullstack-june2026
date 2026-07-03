from pydantic import BaseModel
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
    address:str

class Login(BaseModel):
	email:str
	password:str
