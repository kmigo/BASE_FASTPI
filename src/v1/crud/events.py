from .. import schemas,models
from sqlalchemy.orm import Session
import uuid

def create_event(db:Session,event_data:schemas.EventBase,producer_id:uuid.UUID) -> schemas.Event:
    db_event = models.Event(**event_data.dict(),id=uuid.uuid4(),producer_id=producer_id)
    db.add(db_event)
    db.commit()
    return db_event

def fetch_events(db:Session):
    return db.query(models.Event).all()