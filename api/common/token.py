from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import Header, HTTPException, Depends
from pydantic import BaseModel

# 定义加密上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 定义 JWT 设置
SECRET_KEY = "Afj_hCakVcmKiZCDQNqQ0FkYE_F0B_Lbx69Y98VPJiQ"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class Token(BaseModel):
    access_token: str
    token_type: str


class Login(BaseModel):
    email: str
    password: str


class TokenUser:
    id: int
    email: str


def verify_password(plain_password, hashed_password):
    # pwd_context.encrypt("92a0c93f004fd2dba82823ea05c12428")
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Header(None)) -> TokenUser:
    if token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = TokenUser()
        user.email = payload.get("email")
        if user.email is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        user.id = payload.get("id")
        # 这里可以添加更多的用户验证逻辑
    except JWTError:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return user  # 或者返回用户对象


def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = TokenUser()
        user.email = payload.get("email")
        if user.email is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        user.id = payload.get("id")
        # 这里可以添加更多的用户验证逻辑
    except JWTError:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user  # 或者返回用户对象