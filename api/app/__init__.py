from db import Base, engine
from fastapi import FastAPI
from .okx import okx_router
from .user import user_router

Base.metadata.create_all(bind=engine)


app = FastAPI()

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
