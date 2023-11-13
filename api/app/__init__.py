from fastapi import FastAPI
from .okx import okx_router


app = FastAPI()

app.include_router(
    okx_router,
    prefix="/okx",
    tags=["okx"],
)
