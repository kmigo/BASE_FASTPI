from .. import models,schemas,enums
from sqlalchemy.orm import Session
from sqlalchemy import join, select
import uuid

def create_employee(db:Session, data:schemas.EmployeesEventBase):
    db_model = models.EmployeesEvents(**data.dict(),id=uuid.uuid4())
    db.add(db_model)
    db.commit()
    return db_model
    

def fetch_all_employees(session: Session, pagination:schemas.Pagination = None, search_user_id = None,search_producer_id=None, colums =[models.User] ,status=None):

    # Crie a consulta unindo as três tabelas
    query = (
        # Agora, dizemos quais informações queremos coletar de cada tabela.
        select(
            *colums
        )
        .select_from(
            models.User.__table__
            .join(models.EmployeesEvents.__table__)
            .join(models.Event.__table__)
        )
        .order_by(models.User.id, models.Event.id)
    )
    
    if search_user_id:
        query = query.where(models.User.id == search_user_id)
    if search_producer_id:
        query = query.where(models.Event.producer_id == search_producer_id)
    if pagination:
        query = query.offset(pagination.page * pagination.size).limit(pagination.size)  

    # Execute a consulta e retorne os resultados
    res = session.execute(query).fetchall()
    print(res)
    return res
