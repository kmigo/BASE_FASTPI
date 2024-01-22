from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import routes
from .depends.database import BASE,engine
# create tables
BASE.metadata.create_all(bind=engine)



v1 = FastAPI()

origins = ['*']

v1.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
v1.include_router(routes.users.router)
