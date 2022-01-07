ftx = SpotFtx(
        apiKey='',
        secret='',
        subAccountName=''
    )

ccxt_ftx = ccxt.ftx()
markets = ccxt_ftx.load_markets()
df = pd.DataFrame.from_dict(markets, orient='index')

print("info df avant tri")
print()
print(df.info())

indexNames = df[ df['quote'] != 'USD' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['spot'] == 'False' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['active'] == 'True' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['future'] == 'True' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['type'] != 'spot' ].index
df.drop(indexNames , inplace=True)
# retrait divers
indexNames = df[ df['base'].str.contains('BULL')].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['base'].str.contains('HALF')].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['base'].str.contains('HEDGE')].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['base'].str.contains('BEAR')].index
df.drop(indexNames , inplace=True)

print("info df apres tri")
print()
print(df.info())
print("colonnes utiles df")
mycolumnsdf = ['base','symbol','active','future','spot']
print(df.loc[:,mycolumnsdf])

pairs = df['info']
dict = pairs.to_dict()
dfi = pd.DataFrame.from_dict(dict, orient='index')

print("info dfi avant tri")
print()
print(dfi.info())

dfi['price'] = pd.to_numeric(dfi['price'])
indexNames = dfi[ dfi['enabled'] == 'False' ].index
dfi.drop(indexNames , inplace=True)
indexNames = dfi[ dfi['price'] <0.1 ].index
dfi.drop(indexNames , inplace=True)

print("info dfi apres tri")
print()
print(dfi.info())
print("colonnes utiles dfi")
mycolumnsdfi = ['highLeverageFeeExempt','tokenizedEquity']
print(dfi.loc[:,mycolumnsdfi])

pairList = dfi.name.values.tolist()
print(pairList)
var =  dfi.shape[0]
print("Nombre de cryptos: ", var, "en", df.quote[1])