# ============================================================================
# Import OHLCV data using yahoofinancials
# Author - Mayank Rasu
# =============================================================================

!pip install alpha_vantage
import pandas as pd
from yahoofinancials import YahooFinancials
import datetime
from alpha_vantage.timeseries import TimeSeries

path = "C:\\Users\\jlang\\Desktop\\Bots\\apikey.txt" 

ts = TimeSeries(key=open(path, 'r').read(), output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data.columns= ["open","high","low","close","volume"]