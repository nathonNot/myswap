from fastapi import Depends, FastAPI, HTTPException, Request, Response
from exchange.okex import account, funding


app = FastAPI()


@app.get("/okx/account/balance")
def get_okx_balanc():
    return account.get_balance()


@app.get("/okx/funding/balance")
def get_okx_balanc():
    return funding.get_balances()


@app.get("/okx/funding/valuation")
def get_okx_balanc():
    return funding.get_asset_valuation()
