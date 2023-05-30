import pandas as pd
import yfinance as yf
import pandas_datareader as pdr

from sklearn import preprocessing
import numpy as np

ticker = yf.Ticker('GOOGL').info
print(ticker.keys())

market_cap = ticker['marketCap']
print(market_cap)

market_price = ticker['currentPrice']
previous_close_price = ticker['regularMarketPreviousClose']
print('Ticker: GOOGL')
print('Market Price:', market_price)
print('Previous Close Price:', previous_close_price)


ticker = ['ADBE', 'CL']
#ticker = ['ADBE']
start_date = '2020-01-01'
end_date = '2022-01-01'
G_data = yf.download(ticker, start_date, end_date)
G_data["Date"] = G_data.index
G_data = G_data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
G_data.reset_index(drop=True, inplace=True)

pd.set_option('display.max_columns', None)
print(G_data.tail())

# Import Data in CSV
#G_data.to_csv("GOOGL.csv")

column = G_data.iloc[:, 1]
print(column)
normalized_arr = preprocessing.normalize([column])
print(normalized_arr)
normalized_arr2 = normalized_arr.tolist()
normalized_arr3 = normalized_arr2.split()
#G_data["normalized_arr"] = normalized_arr
print(len(normalized_arr2))



