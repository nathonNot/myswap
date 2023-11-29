
from exchange.binance import UserBinance



usdt_type = ["USDT", "BUSD", "LDUSDT"]
def get_account_balance(user: UserBinance):
    client = user.get_client()
    # account = client.account_snapshot("SPOT")
    # snapshotVos = account["snapshotVos"]
    # balances = snapshotVos[-1]["data"]["totalAssetOfBtc"]
    # price = client.ticker_price("BTCUSDT")
    # asset_balance = float(balances)*float(price["price"]) # 现货账户总额
    # sample_asset_balance = client.simple_account() # 金融和资金账户总额
    # all_balance = asset_balance + float(sample_asset_balance["totalAmountInUSDT"])
    account = client.account()
    total_usdt = 0
    ticker_list = []
    wait_symbol_dc = {}
    for asset in account["balances"]:
        if float(asset["free"]) + float(asset["locked"]) == 0:
            continue
        if asset["asset"] in usdt_type:
            total_usdt = float(asset["free"]) + float(asset["locked"])
        else:
            wait_symbol_dc[asset["asset"]] = float(asset["free"]) + float(asset["locked"])
            ticker_list.append(f"{asset['asset']}USDT")
    ticker_price = client.ticker_price(symbols=ticker_list)
    for ticker in ticker_price:
        total_usdt += float(ticker["price"]) * wait_symbol_dc[ticker["symbol"].replace("USDT", "")]
    print(ticker_price)
    # balance = user.get_client().balance()
    print(total_usdt)
    return ticker_price
