from fastapi import APIRouter, Depends
from exchange.binance import get_current_user_binance, UserBinance
from exchange.binance.account import get_account_balance

binance_router = APIRouter()


@binance_router.get("/balance", description="交易所总余额")
def get_exchange_banlance(user: UserBinance = Depends(get_current_user_binance)):
    
    return get_account_balance(user)