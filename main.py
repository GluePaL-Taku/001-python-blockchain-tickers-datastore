import datetime
from pymongo import MongoClient
from storeData import getDataFromBinance
import os

# make secret file
try:
    secretdir = 'secret'
    os.mkdir(secretdir)
except FileExistsError:
    print('exist')
        
f = open('secret/binance_password.py','w')
f.write("binance_api_key = '" + os.environ['X509'] +  "'")
f.close()
# secret end

client = MongoClient(os.environ['mongouri'],
                     tls=True,
                     tlsCertificateKeyFile='./secret/binance_password.py')

def get_db_handle(db_name):
    db_handle = client[db_name]
    return db_handle

def create_db(db_handle, collection_name, insert_data):
    collection = db_handle[collection_name]
    collection.insert_one(insert_data)

binanceData = { 'date': datetime.datetime.today(), 'data': getDataFromBinance.getBinanceAllTickers() }
create_db(get_db_handle('data'), 'tickers', binanceData)
