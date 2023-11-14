from fastapi import APIRouter
from exchange.okex import account, funding, earning

okx_router = APIRouter()


@okx_router.get("/account/balance", description="资金账户余额")
def get_account_balanc():
    return account.get_balance()


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