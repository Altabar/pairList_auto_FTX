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

ftx = SpotFtx(
        apiKey='',
        secret='',
        subAccountName=''
    )

ftx = ccxt.ftx()
markets = ftx.load_markets()
df = pd.DataFrame.from_dict(markets, orient='index')
# quoteCurrency': 'USD' spot enabled active
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
#print(df.info())
#print("------------------iloc df['info']0 17 (df['info']) :")
#print(df.iloc[0,17])
pairs = df['info']
dict = pairs.to_dict()
dfi = pd.DataFrame.from_dict(dict, orient='index')
#print(dfi.info())
#print("------------------iloc dfi 0 20 (dfi['volumeUsd24h']) :")
#print(dfi.iloc[0,20])
dfi['volumeUsd24h'] = pd.to_numeric(dfi['volumeUsd24h'])
dfi['price'] = pd.to_numeric(dfi['price'])
#exemple plage de prix
indexNames = dfi[ dfi['price'] < 0.0001].index
dfi.drop(indexNames , inplace=True)
#exemple pour l'achat (que des valeurs baissières)
indexNames = dfi[ dfi['change24h'] > 0 ].index
dfi.drop(indexNames , inplace=True)
#retrait des BULL
indexNames = dfi[ dfi['name'].str.contains('BULL')].index
dfi.drop(indexNames , inplace=True)
print(dfi.info())
# la pairList
pairList = dfi.name.values.tolist()
print(pairList)
