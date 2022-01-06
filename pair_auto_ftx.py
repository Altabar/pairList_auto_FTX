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
print()

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
# sur le volume en 24h
#indexNames = dfi[ dfi['volumeUsd24h'] < 6000 ].index
#dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['enabled'] == 'False' ].index
dfi.drop(indexNames , inplace=True)
dfi['change24h'] = pd.to_numeric(dfi['change24h'])
dfi['price'] = pd.to_numeric(dfi['price'])
# exemple plage de prix
#indexNames = dfi[ dfi['price'] < 0.007].index
#dfi.drop(indexNames , inplace=True)
# exemple pour l'achat (que des valeurs baissières)
#indexNames = dfi[ dfi['change24h'] > 0 ].index
#dfi.drop(indexNames , inplace=True)
# retrait divers
indexNames = dfi[ dfi['name'].str.contains('BULL')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['name'].str.contains('HALF')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['name'].str.contains('HEDGE')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['name'].str.contains('BEAR')].index
dfi.drop(indexNames , inplace=True)
#indexNames = dfi[ dfi['name'].str.contains('WBTC')].index
#dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['name'].str.contains('ST')].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['tokenizedEquity'] == 'True' ].index
dfi.drop(indexNames , inplace=True)
#print(dfi.info())
# la pairList
pairList = dfi.name.values.tolist()
print(pairList)
print()
var =  dfi.shape[0]
print("Nombre de cryptos: ", var, "en", df.quote[1])

ftx = SpotFtx(
        apiKey='',
        secret='',
        subAccountName=''
    )

