from db import Base, engine
from fastapi import FastAPI
from .okx import okx_router

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(
    okx_router,
    prefix="/okx",
    tags=["okx"],
)
