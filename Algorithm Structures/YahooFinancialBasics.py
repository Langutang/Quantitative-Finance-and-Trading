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