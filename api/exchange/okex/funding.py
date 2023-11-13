from . import apikey, secretkey, passphrase, flag
import okx.Funding as Funding




def get_funding():
    return Funding.FundingAPI(apikey, secretkey, passphrase, False, flag, debug=False)


def get_balances():
    return get_funding().get_balances()

def get_asset_valuation():
    return get_funding().get_asset_valuation(ccy='USD')
