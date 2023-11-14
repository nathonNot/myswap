from config import local_config

flag = "0"  # 实盘:0 , 模拟盘:1
apikey = local_config["exchange"]["okx"]["api_key"]
secretkey = local_config["exchange"]["okx"]["secret_key"]
passphrase = local_config["exchange"]["okx"]["pass"]

def get_client(init):
    return init(apikey, secretkey, passphrase, False, flag, debug=False)