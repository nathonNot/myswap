from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from db.models_user import get_user_exchange
from binance.spot import Spot

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/token")


class UserBinance:
    user_id: int
    api_key: str
    api_secret: str
    client: Spot

    def __init__(self, user_id: int, api_key: str, api_secret: str):
        self.user_id = user_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Spot(self.api_key, self.api_secret)

    def asset(self):
        return self.client.user_asset()
    
    def get_client(self):
        return self.client

def get_current_user_binance(token: str = Depends(oauth2_scheme)):
    if token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    from common.token import ALGORITHM, SECRET_KEY
    from jose import JWTError, jwt
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        user_exchange = get_user_exchange(user_id, "binance")
        if user_exchange is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        user = UserBinance(user_id, user_exchange.api_key, user_exchange.api_secret)
        user.user_id = user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return user  # 或者返回用户对象
