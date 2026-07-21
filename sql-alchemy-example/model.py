from pydantic import BaseModel
from typing import Optional
class UserRequest(BaseModel):
    id:int
    name:Optional[str]=None
    email:Optional[str]=None
    mobile:Optional[str]=None
    password:Optional[str]=None
    dob:Optional[str]=None

class Login(BaseModel):
    email:str
    password:str