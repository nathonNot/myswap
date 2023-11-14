
from okx import Account


def get_account():
    # API 初始化
    from . import get_client
    accountAPI = get_client(Account.AccountAPI)
    return accountAPI


def get_balance():
    return get_account().get_account_balance()
