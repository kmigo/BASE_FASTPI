from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .. import routes,schemas
from ..depends.database import get_db
from typing import List
router = APIRouter(prefix='/users',tags=['USERS'])

@router.get('/',response_model=List[schemas.User])
def fetch_users(db :Session= Depends(get_db)):
    return []