"""
Created on Sun Mar 29 12:37:09 2020

@author: jlang
"""

####################################################
################ MACD INDICATOR ####################
####################################################

import pandas_datareader.data as pdr
import datetime

ticker = 'MSFT'
ohlcv = pdr.get_data_yahoo(ticker, 
                           datetime.date.today()-datetime.timedelta(1825),
                           datetime.date.today())

def MACD(DF, a,b,c):
    df = ohlcv.copy()
    df['MA_Fast']=df["Adj Close"].ewm(span=12).mean()
    df['MA_Slow']=df["Adj Close"].ewm(span=26).mean()
    df["MACD"] = df["MA_Fast"]-df["MA_Slow"]
    df["Signal"] = df["MACD"].ewm(span=9,min_periods=9).mean()
    df.dropna(inplace=True)
    return df

MACD(ohlcv,12,26,9)

####################################################
################ MACD PLOTTING  ####################
####################################################

df = ohlcv.copy()
df['MA_Fast']=df["Adj Close"].ewm(span=12).mean()
df['MA_Slow']=df["Adj Close"].ewm(span=26).mean()
df["MACD"] = df["MA_Fast"]-df["MA_Slow"]
df["Signal"] = df["MACD"].ewm(span=9,min_periods=9).mean()
df.dropna(inplace=True)
return df

df.iloc[:,[5,8,9]].plot()
df.iloc[:,[5,8,9]].plot(subplots=True, layout=(3,1))