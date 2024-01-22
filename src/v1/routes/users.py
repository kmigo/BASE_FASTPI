from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..schemas import users
from ..depends.database import get_db
from typing import List
from .. import crud
router = APIRouter(prefix='/users',tags=['USERS'])

@router.get('',response_model=List[users.User])
def fetch_users(session :Session= Depends(get_db)):
    return crud.users.get_users(session)


@router.post('',response_model=users.User)
def create_user(user:users.UserCreate,session :Session= Depends(get_db)):
    return crud.users.create_user(session,user)