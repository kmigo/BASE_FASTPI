from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import routes,models
from .depends import database
models.BASE.metadata.create_all(bind=database.engine)
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
v1.include_router(routes.events.router)
v1.include_router(routes.administrative.router)
