import json

local_config = {}

def get_config():
    global local_config
    return local_config

def load_config():
    global local_config
    local_config = json.load(open('config.json', 'r'))
    print(local_config)
    
load_config()