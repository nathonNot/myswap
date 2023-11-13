from fastapi import APIRouter
from exchange.okex import account, funding

okx_router = APIRouter()

@okx_router.get("/account/balance")
def get_okx_balanc():
    return account.get_balance()


@okx_router.get("/funding/balance")
def get_okx_balanc():
    return funding.get_balances()


@okx_router.get("/funding/valuation")
def get_okx_balanc():
    return funding.get_asset_valuation()
