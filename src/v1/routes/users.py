from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from .. import routes,schemas,crud
from ..depends.database import get_db
from typing import List
router = APIRouter(prefix='/users',tags=['USERS'])

@router.get('/',response_model=List[schemas.User])
def fetch_users(db :Session= Depends(get_db)):
    return crud.users.fetch_users(db)

@router.post('/create',response_model=schemas.User,status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.UserBase,db=Depends(get_db)):
    return crud.users.create_user(db,user)