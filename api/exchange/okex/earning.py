
from okx import Funding, Earning
from . import get_client
# 金融产品相关


def get_earning():
    return get_client(Earning.EarningAPI)


def get_order():
    return get_earning().get_activity_orders()


def get_offers():
    return get_earning().get_offers()

# 余币宝


def get_savings_balance():
    fundingAPI = get_client(Funding.FundingAPI)
    return fundingAPI.get_saving_balance()
