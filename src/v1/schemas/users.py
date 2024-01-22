from pydantic import BaseModel
from typing import List,Union

class Token(BaseModel):
    access_token: str
    token_type: str
    
"""
Nome 
Telefone 
E-mail
Nome do negocio
"""

class UserBase(BaseModel):
    name:str
    phone:str
    email:str
    name_business:str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: Union[str, None] = None
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: Union[str, None] = None
    scopes: List[str] = []