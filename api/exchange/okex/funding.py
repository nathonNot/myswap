from . import get_client
from okx import Funding

def get_funding():
    return get_client(Funding.FundingAPI)


def get_balances():
    return get_funding().get_balances()

def get_asset_valuation():
    return get_funding().get_asset_valuation(ccy='USD')
