from dotenv import load_dotenv
from fastapi import FastAPI
load_dotenv()
from .v1.router import v1


app = FastAPI()

app.mount('/v1',v1)
