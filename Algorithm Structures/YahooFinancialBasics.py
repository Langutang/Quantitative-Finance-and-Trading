# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:56:39 2020

@author: jlang
"""

import pandas as pd
from yahoofinancials import YahooFinancials
import datetime

all_tickers = ['AAPL','AMZN','CSCO','MSFT','INTC']

close_prices = pd.DataFrame()
end_date = (datetime.date.today()).strftime('%Y-%m-%d')
start_date = (datetime.date.today()-datetime.timedelta(180)).strftime('%Y-%m-%d')
cp_tickers = all_tickers
attempt = 0
drop = []

aapl = YahooFinancials("AAPL")
aapl

while len(cp_tickers) != 0 and attempt <=5:
    print("-----------------")
    print("attempt number ",attempt)
    print("-----------------")
    cp_tickers = [j for j in cp_tickers if j not in drop]
    for i in range(len(cp_tickers)):
        try:
            yahoo_financials = YahooFinancials(cp_tickers[i])
            json_obj = yahoo_financials.get_historical_price_data(start_date, end_date, "daily")
            ohlv = json_obj[cp_tickers[i]]['prices']
            temp = pd.DataFrame(ohlv)[["formatted_date", "adjclose"]]
            temp.set_index("formatted_date",inplace=True)
            temp2 = temp[~temp.index.duplicated(keep='first')]
            close_prices[cp_tickers[i]] = temp2["adjclose"]
            drop.append(cp_tickers[i])
        except:
            print(cp_tickers[i],"    :failed to fetch data... retrying")
            continue
    attempt+=1
    
    
###############################################################################
######################## AAPL TICKER TEST######################################
###############################################################################

yahoo_financials = YahooFinancials("AAPL")
json_obj = yahoo_financials.get_historical_price_data(start_date, end_date, "daily")
ohlv = json_obj["AAPL"]['prices']
temp = pd.DataFrame(ohlv)[["formatted_date", "adjclose"]]
temp.set_index("formatted_date",inplace=True)
temp2 = temp[~temp.index.duplicated(keep='first')]
close_prices[cp_tickers[i]] = temp2["adjclose"]
drop.append(cp_tickers[i])

###############################################################################
######################## DATA FAMILIARIZATION #################################
###############################################################################

close_prices.mean(axis=0)
close_prices.median(axis=0)
close_prices.std(axis=0)

# We need daily returns - how much a stock yielded daily over time period
daily_return = close_prices.pct_change()
daily_return.mean(axis=0)
daily_return.std(axis=0)

###############################################################################
######################## ROLLING MEAN AND STD #################################
###############################################################################

# How does a mean and std move over a given time period
daily_return.rolling(window=20, min_periods=1).mean()
daily_return.rolling(window=20).std()
#Exponential moving average
daily_return.ewm(span=20, min_periods=20).mean() #simple exponeital MA
daily_return.ewm(span=20, min_periods=20).std()

# Visualization
close_prices.plot()
cp_standardized = (close_prices - close_prices.mean())/close_prices.std()
cp_standardized.plot()

close_prices.plot(subplots = True, layout = (3,2))
# We need daily returns - how much a stock yielded daily over time period
daily_return = close_prices.pct_change()
daily_return.mean(axis=0)
daily_return.std(axis=0)
