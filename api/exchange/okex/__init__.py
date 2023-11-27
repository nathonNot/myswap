from fastapi import Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
from config import local_config
from db.models_user import get_user_exchange
from okx import Account, Funding, Earning

flag = "0"  # 实盘:0 , 模拟盘:1
# apikey = local_config["exchange"]["okx"]["api_key"]
# secretkey = local_config["exchange"]["okx"]["secret_key"]
# passphrase = local_config["exchange"]["okx"]["pass"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/token")


class UserOkx:
    user_id: int
    api_key: str
    api_secret: str
    api_passphrase: str

    def __init__(self) -> None:
        pass

    def __init__(self, user_id: int, api_key: str, api_secret: str, api_passphrase: str):
        self.user_id = user_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase

    def _get_client(self, init):
        return init(self.api_key, self.api_secret, self.api_passphrase, False, flag, debug=False)

    def get_account(self) -> Account.AccountAPI:
        return self._get_client(Account.AccountAPI)

    def get_funding(self) -> Funding.FundingAPI:
        return self._get_client(Funding.FundingAPI)

    def get_earing(self) -> Earning.EarningAPI:
        return self._get_client(Earning.EarningAPI)


def get_current_user_okx(token: str = Depends(oauth2_scheme)):
    if token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    from common.token import ALGORITHM, SECRET_KEY
    from jose import JWTError, jwt
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        user_okx = UserOkx()
        user_okx.user_id = user_id
        user_exchange = get_user_exchange(user_id, "okx")
        if user_exchange:
            user_okx.api_key = user_exchange.api_key
            user_okx.api_secret = user_exchange.api_secret
            user_okx.api_passphrase = user_exchange.api_passphrase
    except JWTError:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return user_okx  # 或者返回用户对象
