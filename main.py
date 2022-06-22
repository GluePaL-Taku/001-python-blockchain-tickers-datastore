import datetime
from pymongo import MongoClient
from storeData import getDataFromBinance

client = MongoClient(os.environ['mongouri'],
                     tls=True,
                     tlsCertificateKeyFile=os.environ['X509'])

def get_db_handle(db_name):
    db_handle = client[db_name]
    return db_handle

def create_db(db_handle, collection_name, insert_data):
    collection = db_handle[collection_name]
    collection.insert_one(insert_data)

binanceData = { 'date': datetime.datetime.today(), 'data': getDataFromBinance.getBinanceAllTickers() }
create_db(get_db_handle('data'), 'tickers', binanceData)
