import sys
sys.path.append('cBot-Project/utilities')
from custom_indicators import CustomIndocators as ci
from spot_ftx import SpotFtx
import pandas as pd
import ta
import ccxt
from datetime import datetime
import time
import numpy as np

pd.options.display.max_rows = 200
pd.options.display.max_columns =100

now = datetime.now()
print(now.strftime("%d-%m %H:%M:%S"))

ftx = ccxt.ftx()
markets = ftx.load_markets()
df = pd.DataFrame.from_dict(markets, orient='index')
indexNames = df[ df['quote'] != 'USD' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['spot'] == 'False' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['active'] == 'False' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['future'] == 'True' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['type'] != 'spot' ].index
df.drop(indexNames , inplace=True)
pairs = df['info']
dict = pairs.to_dict()
dfi = pd.DataFrame.from_dict(dict, orient='index')
dfi['volumeUsd24h'] = pd.to_numeric(dfi['volumeUsd24h'])
indexNames = dfi[ dfi['enabled'] == 'False' ].index
dfi.drop(indexNames , inplace=True)
dfi['change24h'] = pd.to_numeric(dfi['change24h'])
dfi['price'] = pd.to_numeric(dfi['price'])
# retrait divers
indexNames = dfi[ dfi['name'].str.contains('BULL')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['name'].str.contains('HALF')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['name'].str.contains('HEDGE')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['name'].str.contains('BEAR')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['name'].str.contains('ST')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['tokenizedEquity'] == 'True' ].index
dfi.drop(indexNames , inplace=True)
#print(dfi.info())
pairList = dfi.name.values.tolist()
print(pairList)
var =  dfi.shape[0]
print("Nombre de cryptos: ", var, "en", df.quote[1])

ftx = SpotFtx(
        apiKey='',
        secret='',
        subAccountName=''
    )

