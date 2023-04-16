from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from .. import schemas,crud,enums
from ..depends.database import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix='/administrative',tags=['ADMINISTRATIVO'])

@router.get('/employees/users',status_code=status.HTTP_200_OK,response_model=List[schemas.User])
def fetch_employees_users(page: int =None,status:  enums.EmployeesEventStatus = None,size:int=None,search_user_id:str=None,db :Session= Depends(get_db)):
    return crud.administrative.fetch_all_employees(db,pagination= schemas.Pagination(page=page,size=size) if page and size else None,search_user_id=search_user_id)

@router.post('/employees/create',response_model=schemas.EmployeesEvent,status_code=status.HTTP_201_CREATED)
def create_employee(employee:schemas.EmployeesEventBase,db=Depends(get_db)):
    return crud.administrative.create_employee(db,employee)