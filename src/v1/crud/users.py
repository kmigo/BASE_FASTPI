from .. import schemas,models
from sqlalchemy.orm import Session
import uuid
 
def create_user(db:Session,user_data:schemas.UserBase) -> schemas.User:
    db_user = models.User(**user_data.dict(),id=uuid.uuid4())
    db.add(db_user)
    db.commit()
    return db_user

def fetch_users(db:Session):
    return db.query(models.User).all()