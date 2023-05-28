
# Import Libraries

import numpy as np
import datetime
from datetime import timedelta
import pandas as pd
import yfinance as yf
import requests


# Set individual

#np.random.seed(8390715)
start_date = datetime.date(2020, 4, 1) - timedelta(days = np.random.randint(20))
start_date.strftime("%Y-%m-%d")
end_date = datetime.date(2021, 4, 1) + timedelta(days = np.random.randint(20))
end_date.strftime("%Y-%m-%d")

# get tickers from Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[0]
pd.set_option('display.max_columns', None)
#print(df)
#df.to_csv('my data.csv')

# extract first row
ticker = df["Symbol"]
#print(ticker)
ticker_as_list = ticker.tolist()
#print(ticker_as_list)

# Import Stock Data from Yahoo

start_date = '2023-01-01'
end_date = '2023-04-01'
SP500 = yf.download(ticker_as_list, start_date, end_date)
SP500["Date"] = SP500.index
SP500 = SP500[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
SP500.reset_index(drop=True, inplace=True)

pd.set_option('display.max_columns', None)
#print(SP500.tail())
SP500.to_csv("S&P500.csv")


