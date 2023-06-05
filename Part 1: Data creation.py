
# Import Libraries

import numpy as np
import datetime
from datetime import timedelta
import pandas as pd
import yfinance as yf
import requests


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
ticker_as_list = ticker.tolist()
ticker_as_list.append("^GSPC")

# Import Stock Data
ticker1 = ["ticker_as_list"]
start_date = '2020-05-01'
end_date = '2021-05-01'
SP500 = yf.download(ticker_as_list, start_date, end_date)
SP500["Date"] = SP500.index
SP500 = SP500[["Date", "Close", "Volume", "High", "Low", "Open", "Adj Close"]]
SP500.reset_index(drop=True, inplace=True)
pd.set_option('display.max_columns', None)
#SP500.to_csv("S&P500.csv")

# Count Stocks
start_date_count = '2023-01-01'
end_date_count = '2023-05-01'
SP500_count = yf.download(ticker_as_list, start_date, end_date)
SP500_count = SP500["Close"]
SP500_count.to_csv("S&P500_count.csv")
column_header = (list(SP500_count.columns))
Count_Stocks = str(len(column_header))

# Normalize Data
#for i in range(1,len(column_header)+1):
#    SP500.iloc[:,i] = SP500.iloc[:,i].apply(lambda x: x / abs(max(SP500.iloc[:,i])))

#for i in range(1,len(column_header)+1):
#    SP500.iloc[:,i] = SP500.iloc[:,i].apply(lambda x: (x - SP500.iloc[:,i].mean()) / SP500.iloc[:,i].std())


Stock_Names = column_header
file = open(("Stock_Names.txt"), "w")
file.write(str(Stock_Names))
file.close()

file = open("Stock_Count.txt", "w")
file.write(str(Count_Stocks))
file.close()

SP500.to_csv('S&P500.csv')
print(SP500.tail)



