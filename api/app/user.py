from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from common.token import Token, Login, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_password, verify_token
from db import get_db
from db.models_user import User

user_router = APIRouter()


@user_router.post("/login", response_model=Token)
def login_for_access_token(form_data: Login, db: Session = Depends(get_db)):
    if form_data.email == "":
        raise HTTPException(status_code=400, detail="Email cannot be empty")
    user = db.query(User).filter(User.email == form_data.email).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": user.email,
              "id": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/check")
def check_token(token: str):
    verify_token(token)
    return "ok"
