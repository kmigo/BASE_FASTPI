from fastapi_utils.guid_type import GUID
from sqlalchemy.sql import func
from datetime import datetime
from .depends.database import BASE
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from . import enums


class Serializer:
    def dict(self):
        output = {}
        for k, v in self.__dict__.items():
            if k.startswith('_'):
                continue
            if isinstance(v, datetime):
                output[k] = str(v)
            else:
                output[k] = v
        return output


class User(BASE, Serializer):
    __tablename__ = 'users'
    id = sa.Column(
        GUID,
        primary_key=True, nullable=False,unique=True
    )
    name = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String,nullable=False,unique=True)

class Event(BASE, Serializer):
    __tablename__ = 'events'
    id = sa.Column(
        GUID,
        primary_key=True, nullable=False,unique=True
    )
    name = sa.Column(
        sa.String, nullable=False
    )
    producer_id = sa.Column(GUID,nullable=False)


class EmployeesEvents(BASE, Serializer):
    __tablename__ = 'employees_events'
    id = sa.Column(
        GUID,
        primary_key=True,unique=True
    )
    user_id = sa.Column(GUID, sa.ForeignKey('users.id'))
    event_id = sa.Column(GUID, sa.ForeignKey('events.id'))
    status = sa.Column(sa.Enum(enums.EmployeesEventStatus), nullable=False)
