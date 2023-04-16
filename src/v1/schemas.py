from pydantic import BaseModel
from typing import List,Union
from uuid import UUID
from . import enums
class Pagination(BaseModel):
    page:int
    size:int

class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserBase(BaseModel):
    name:str

    class Config:
        orm_mode=True

class User(UserBase):
    id:UUID
    class Config:
        orm_mode=True

class EventBase(BaseModel):
    name:str
    class Config:
        orm_mode=True
class Event(EventBase):
    id :UUID

    class Config:
        orm_mode=True

class TokenData(BaseModel):
    id: Union[str, None] = None
    scopes: List[str] = []

class EmployeesEventBase(BaseModel):

    user_id :UUID
    event_id :UUID
    status : enums.EmployeesEventStatus
    class Config:
        orm_mode=True

class EmployeesEvent(EmployeesEventBase):
    id :UUID
    
    class Config:
        orm_mode=True