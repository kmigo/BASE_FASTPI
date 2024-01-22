from src.v1.depends.database import BASE
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
class Serializer:
    def dict(self):
        output = {}
        for k,v in self.__dict__.items():
            if k.startswith('_'):continue
            if isinstance(v,datetime):
                output[k] = str(v)
            elif isinstance(v,uuid.UUID):
                output[k] = str(v)
            elif isinstance(v,Serializer):
                output[k] = v.model_dump()
            elif isinstance(v,BASE):
                output[k] = v.model_dump()
            else:
                output[k] = v
        return output
    def model_dump(self):
        output = {}
        for k,v in self.__dict__.items():
            if k.startswith('_'):continue
            if isinstance(v,datetime):
                output[k] = str(v)
            elif isinstance(v,uuid.UUID):
                output[k] = str(v)
            elif isinstance(v,Serializer):
                output[k] = v.model_dump()
            elif isinstance(v,BASE):
                output[k] = v.model_dump()
            else:
                output[k] = v
        return output

class User(BASE,Serializer):
    __tablename__ = 'users'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    name_business = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())