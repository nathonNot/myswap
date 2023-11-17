from fastapi import HTTPException, Header
from config import local_config

flag = "0"  # 实盘:0 , 模拟盘:1
# apikey = local_config["exchange"]["okx"]["api_key"]
# secretkey = local_config["exchange"]["okx"]["secret_key"]
# passphrase = local_config["exchange"]["okx"]["pass"]

apikey = ""
secretkey = ""
passphrase = ""


def get_client(init):
    return init(apikey, secretkey, passphrase, False, flag, debug=False)


class UserOkx:
    user_id: int
    api_key: str
    api_secret: str
    api_passphrase: str

def get_current_user_okx(token: str = Header(None)):
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
    except JWTError:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return user_okx  # 或者返回用户对象
