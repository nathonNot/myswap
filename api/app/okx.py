from fastapi import APIRouter, Depends
from exchange.okex import account, funding, earning, get_current_user_okx, UserOkx

okx_router = APIRouter()


@okx_router.get("/account/balance", description="资金账户余额")
def get_account_balanc(user_okx: UserOkx = Depends(get_current_user_okx)):
    # return account.get_balance()
    return user_okx


@okx_router.get("/funding/balance", description="资金账户余额")
def get_funding_balanc():
    return funding.get_balances()


@okx_router.get("/funding/valuation", description="资金账户估值")
def get_funding_valuation():
    return funding.get_asset_valuation()


@okx_router.get("/earning/offers", description="金融产品项目")
def get_earning_offers():
    return earning.get_offers()


@okx_router.get("/earning/orders-active", description="金融产品活跃订单")
def get_earning_orders_active():
    return earning.get_order()


@okx_router.get("/funding/saving-balance", description="余币宝余额")
def get_funding_saving_balance():
    return earning.get_savings_balance()


@okx_router.get("/balance", description="交易所账户余额")
def get_exchange_banlance():
    return funding.get_asset_valuation()
