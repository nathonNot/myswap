
import okx.Account as Account





def get_account():
    # API 初始化
    from . import apikey, secretkey, passphrase, flag
    accountAPI = Account.AccountAPI(
        apikey, secretkey, passphrase, False, flag, debug=False)
    return accountAPI


def get_balance():
    return get_account().get_account_balance()
