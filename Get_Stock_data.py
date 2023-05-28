import pandas as pd
import yfinance as yf
import pandas_datareader as pdr

ticker = yf.Ticker('GOOGL').info
print(ticker.keys())

market_cap = ticker['marketCap']
print(market_cap)

market_price = ticker['currentPrice']
previous_close_price = ticker['regularMarketPreviousClose']
print('Ticker: GOOGL')
print('Market Price:', market_price)
print('Previous Close Price:', previous_close_price)


ticker = ['GOOGL']
start_date = '2020-01-01'
end_date = '2022-01-01'
G_data = yf.download(ticker, start_date, end_date)
G_data["Date"] = G_data.index
G_data = G_data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
G_data.reset_index(drop=True, inplace=True)

pd.set_option('display.max_columns', None)
print(G_data.tail())

#import Data in CSV
#G_data.to_csv("GOOGL.csv")


