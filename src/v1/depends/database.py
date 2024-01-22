from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

def _get_sgbd():
    sgbd = os.getenv('DB_ENGINE')
    assert sgbd != None ,'Variable Environment Erro, DB_SGBD is None'
    assert sgbd in ['mysql+pymysql','postgresql','sqlite'] , 'Variable Environment Error, DB_SGBD should be  "postgresql" or "mysql+pymysql"'
    return sgbd

sqlalchemy_database_url = f"{_get_sgbd()}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine  = create_engine(os.environ.get('DATABASE_URL',sqlalchemy_database_url)) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BASE = declarative_base()



# Dependency
def get_db() :
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()