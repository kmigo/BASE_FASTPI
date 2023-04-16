from dotenv import load_dotenv
from fastapi import FastAPI
load_dotenv()
from .v1.router import v1
import logging
# Configurar o nível de registro para o logger do SQLAlchemy
logging.getLogger("sqlalchemy").setLevel(logging.ERROR)

app = FastAPI()

app.mount('/v1',v1)
