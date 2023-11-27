from db import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .okx import okx_router
from .user import user_router

Base.metadata.create_all(bind=engine)


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://8.222.188.249:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    okx_router,
    prefix="/api/okx",
    tags=["okx"],
)

app.include_router(
    user_router,
    prefix="/api/user",
    tags=["user"],
)

import common