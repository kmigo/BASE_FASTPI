from sqlalchemy.orm import Session
from src.v1 import schemas,models
from typing import List

def get_users(session:Session) -> List[schemas.users.User]:
    users = session.query(models.User).all()
    users = [schemas.users.User(**user.__dict__) for user in users]
    return users

def create_user(session:Session,user:schemas.users.User) -> schemas.users.User:
    user = models.User(**user.__dict__)
    session.add(user)
    session.commit()
    session.refresh(user)
    return schemas.users.User.from_orm(user)