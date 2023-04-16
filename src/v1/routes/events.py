from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from .. import routes,schemas,crud
from ..depends.database import get_db
from typing import List
from uuid import UUID
router = APIRouter(prefix='/events',tags=['EVENTS'])

@router.get('/',response_model=List[schemas.Event])
def fetch_events(db :Session= Depends(get_db)):
    return crud.events.fetch_events(db)

@router.post('/producer/{producer_id}/create',response_model=schemas.Event,status_code=status.HTTP_201_CREATED)
def create_events(producer_id: UUID,event:schemas.EventBase,db=Depends(get_db)):
    return crud.events.create_event(db,event,producer_id)