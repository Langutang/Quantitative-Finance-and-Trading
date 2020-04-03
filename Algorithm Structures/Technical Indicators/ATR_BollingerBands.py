# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:06:21 2020

@author: jlang
"""

###########################################
############ ATR / BOLLINGER BANDS ########
###########################################

# Bollinger bands comprises of two lines at n std above ma, and m std below ma
# ATR takes into acocunt the market movement each day

# Typically used in conjunction as they approach volatility differently

import pandas_datareader.data as pdr
import datetime

ticker = "MSFT"

ohlcv = pdr.get_data_yahoo(ticker,
                           datetime.date.today()-datetime.timedelta(1825),
                           datetime.date.today())

###########################################
############ ATR ##########################
###########################################

def ATR(DF,n):
    df = DF.copy()
    df['H-L']=abs(df['High']-df['Low'])
    df['H-PC']=abs(df['High']-df['Adj Close']).shift(1)
    df['L-PC']=abs(df['Low']-df['Adj Close']).shift(1)
    df['TR']=df[['H-L','H-PC','L-PC']].max(axis=1,skipna=False)
    df['ATR'] = df['TR'].rolling(n).mean()
    
    df2 = df.drop(['H-L','H-PC','L-PC'], axis=1)
    return df2

ATR(ohlcv,20)

###########################################
############ BOLLINGER BANDS ##############
###########################################

def BollBands(DF,n):
    df = DF.copy()
    df['MA'] = df['Adj Close'].rolling(n).mean()
    df['BB_up'] =  df['MA'] + df['MA'].rolling(n).std()
    df['BB_down'] = df['MA'] - df['MA'].rolling(n).std()
    df['BB_range'] = df['BB_up'] - df['BB_down']
    df.dropna(inplace = True)
    return df

BollBands(ohlcv, 2)

BollBands(ohlcv, 20).iloc[-100:,[-4,-3,-2]].plot()
