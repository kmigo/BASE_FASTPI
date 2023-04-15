from pydantic import BaseModel
from typing import List,Union

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    id:int
    name:str
    disabled:str

class TokenData(BaseModel):
    id: Union[str, None] = None
    scopes: List[str] = []