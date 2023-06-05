# Import Libraries

import numpy as np
import datetime
from datetime import timedelta
import pandas as pd
import yfinance as yf
import requests

import bokeh
from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import show
from bokeh.models import DatetimeTickFormatter
from math import pi
from bokeh.models import HoverTool
from bokeh.plotting import ColumnDataSource

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

# Import Stock random Data from Yahoo

random_ticker = np.random.choice(ticker_as_list, 9, replace=False)
#print(random_ticker)
random_ticker_as_list = random_ticker.tolist()
print(random_ticker_as_list)

start_date = '2020-05-01'
end_date = '2021-05-01'
SP500 = yf.download(random_ticker_as_list, start_date, end_date)
SP500["Date"] = SP500.index
SP500 = SP500[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
SP500.reset_index(drop=True, inplace=True)

pd.set_option('display.max_columns', None)
#print(SP500.tail)
#SP500.to_csv("S&P500.csv")

# Normalize Data
SP500.iloc[:,1] = SP500.iloc[:,1].apply(lambda x: x / abs(max(SP500.iloc[:,1])))
SP500.iloc[:,2] = SP500.iloc[:,2].apply(lambda x: x / abs(max(SP500.iloc[:,2])))
SP500.iloc[:,3] = SP500.iloc[:,3].apply(lambda x: x / abs(max(SP500.iloc[:,3])))
SP500.iloc[:,4] = SP500.iloc[:,4].apply(lambda x: x / abs(max(SP500.iloc[:,4])))
SP500.iloc[:,5] = SP500.iloc[:,5].apply(lambda x: x / abs(max(SP500.iloc[:,5])))
SP500.iloc[:,6] = SP500.iloc[:,6].apply(lambda x: x / abs(max(SP500.iloc[:,6])))
SP500.iloc[:,7] = SP500.iloc[:,7].apply(lambda x: x / abs(max(SP500.iloc[:,7])))
SP500.iloc[:,8] = SP500.iloc[:,8].apply(lambda x: x / abs(max(SP500.iloc[:,8])))
SP500.iloc[:,9] = SP500.iloc[:,9].apply(lambda x: x / abs(max(SP500.iloc[:,9])))

column_header = (list(SP500.columns))
concat_df = pd.DataFrame()

for i in range(2,10):
    new_row = zip(SP500.iloc[:,0], SP500.iloc[:,i])
    new_dataframe = pd.DataFrame(list(new_row))
    new_dataframe["Ticker"] = (column_header[i][1])
    new_dataframe.columns = ["Date", "Opening_Value", "Ticker"]
    new_dataframe_right_order = new_dataframe.iloc[:, [2, 0, 1]]
    concat_df = pd.concat([concat_df, new_dataframe_right_order])

concat_df.to_csv("Test.csv")
print(concat_df)