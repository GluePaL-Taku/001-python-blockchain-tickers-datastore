# for binance
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json
import os

# # for password
# import sys
# sys.path.append("./secret")
# import binance_password
# # From secret/binance_password.py module
# api_key = binance_password.binance_api_key
# api_secret = binance_password.binance_api_secret

# client = Client(api_key, api_secret)


client = Client(os.environ['api_key'], os.environ['api_secret'])

def getBinanceAllTickers():
    return json.dumps(client.get_all_tickers())
