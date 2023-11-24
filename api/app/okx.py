from fastapi import APIRouter, Depends
from exchange.okex import get_current_user_okx, UserOkx

okx_router = APIRouter()


@okx_router.get("/account/balance", description="资金账户余额")
def get_account_balanc(user_okx: UserOkx = Depends(get_current_user_okx)):
    return user_okx.get_account().get_account_balance()

@okx_router.get("/funding/balance", description="资金账户余额")
def get_funding_balanc(user_okx: UserOkx = Depends(get_current_user_okx)):
    return user_okx.get_funding().get_balances()

@okx_router.get("/funding/valuation", description="资金账户估值")
def get_funding_valuation(user_okx: UserOkx = Depends(get_current_user_okx)):
    return user_okx.get_funding().get_asset_valuation("usdt")

@okx_router.get("/earning/offers", description="金融产品项目")
def get_earning_offers(user_okx: UserOkx = Depends(get_current_user_okx)):
    return user_okx.get_earing().get_offers()

@okx_router.get("/earning/orders-active", description="金融产品活跃订单")
def get_earning_orders_active(user_okx: UserOkx = Depends(get_current_user_okx)):
    return user_okx.get_earing().get_activity_orders()

@okx_router.get("/funding/saving-balance", description="总余额")
def get_funding_saving_balance(user_okx: UserOkx = Depends(get_current_user_okx)):
    return user_okx.get_funding().get_saving_balance()

@okx_router.get("/balance", description="交易所总余额")
def get_exchange_banlance(user_okx: UserOkx = Depends(get_current_user_okx)):
    return user_okx.get_funding().get_saving_balance()
