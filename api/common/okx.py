

from db import get_db_session
from db.models_user import UserExchange, UserFundsChange
from exchange.okex import UserOkx


def update_okx_funding_balance():
    db = get_db_session()
    all_users = db.query(UserExchange).all()
    for u in all_users:
        user = UserOkx(u.user_id, u.api_key, u.api_secret, u.api_passphrase)
        user_okx = user.get_funding().get_asset_valuation("usdt")
        if user_okx["code"] != "0":
            continue
        earn = user_okx["data"][0]["details"]["earn"]
        funding = user_okx["data"][0]["details"]["funding"]
        trading = user_okx["data"][0]["details"]["trading"]
        UserFundsChange(user_id=u.user_id, exchange="okx", change_num=earn, ext="earn_update").save()
        UserFundsChange(user_id=u.user_id, exchange="okx", change_num=funding, ext="funding_update").save()
        UserFundsChange(user_id=u.user_id, exchange="okx", change_num=trading, ext="trading_update").save()
            