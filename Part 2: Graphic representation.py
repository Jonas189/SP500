
# Import Libraries

import numpy as np
import datetime
from datetime import timedelta
import pandas as pd
import yfinance as yf
import requests
import math

import bokeh
from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import show
from bokeh.models import DatetimeTickFormatter
from math import pi
from bokeh.models import HoverTool
from bokeh.plotting import ColumnDataSource



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

# extract first row
ticker = df["Symbol"]
ticker_as_list = ticker.tolist()

# Import Stock random Data from Yahoo

random_ticker = np.random.choice(ticker_as_list, 9, replace=False)
random_ticker_as_list = random_ticker.tolist()
print(random_ticker_as_list)

start_date = '2020-05-01'
end_date = '2021-05-01'
SP500 = yf.download(random_ticker_as_list, start_date, end_date)
SP500["Date"] = SP500.index
SP500 = SP500[["Date", "Close", "Volume", "High", "Low", "Open", "Adj Close"]]
SP500.reset_index(drop=True, inplace=True)

pd.set_option('display.max_columns', None)

column_header = (list(SP500.columns))


#SP500.to_csv("S&P500_test.csv")

# Normalize Data
#SP500.iloc[:,1] = SP500.iloc[:,1].apply(lambda x: (x - SP500.iloc[:,1].mean()) / SP500.iloc[:,1].std())
#SP500.iloc[:,2] = SP500.iloc[:,2].apply(lambda x: (x - min(SP500.iloc[:,2]) / (max(SP500.iloc[:,2]) - min(SP500.iloc[:,2]))))
#SP500.iloc[:,1] = SP500.iloc[:,1].apply(lambda x: x / abs(max(SP500.iloc[:,1])))
#SP500.iloc[:,2] = SP500.iloc[:,2].apply(lambda x: x / abs(max(SP500.iloc[:,2])))
#SP500.iloc[:,3] = SP500.iloc[:,3].apply(lambda x: x / abs(max(SP500.iloc[:,3])))
#SP500.iloc[:,4] = SP500.iloc[:,4].apply(lambda x: x / abs(max(SP500.iloc[:,4])))
#SP500.iloc[:,5] = SP500.iloc[:,5].apply(lambda x: x / abs(max(SP500.iloc[:,5])))
#SP500.iloc[:,6] = SP500.iloc[:,6].apply(lambda x: x / abs(max(SP500.iloc[:,6])))
#SP500.iloc[:,7] = SP500.iloc[:,7].apply(lambda x: x / abs(max(SP500.iloc[:,7])))
#SP500.iloc[:,8] = SP500.iloc[:,8].apply(lambda x: x / abs(max(SP500.iloc[:,8])))
#SP500.iloc[:,9] = SP500.iloc[:,9].apply(lambda x: x / abs(max(SP500.iloc[:,9])))


# Visualization
SP500.index = SP500.index.astype(str)

p = figure(title = "S&P500 Example", x_axis_label = 'Time', x_axis_type="datetime", y_axis_label = 'Scaled Prices',width=800, tools='hover, pan, zoom_out, zoom_in, reset, crosshair')
formatters={'x': 'datetime'}
p.line(SP500.iloc[:,0], SP500.iloc[:,1], legend_label = str((column_header[1][1])), color ="red", line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,2], legend_label = str((column_header[2][1])), color ="green", line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,3], legend_label = str((column_header[3][1])), color ="blue", line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,4], legend_label = str((column_header[4][1])), color ="orange", line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,5], legend_label = str((column_header[5][1])), line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,6], legend_label = str((column_header[6][1])), line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,7], legend_label = str((column_header[7][1])), line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,8], legend_label = str((column_header[8][1])), line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,9], legend_label = str((column_header[9][1])), line_width = 2)
p.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    )
p.xaxis.major_label_orientation = pi/4

# Visualization Adjustments
p.legend.location = "top_left"
p.legend.title = "S&P-500 Symbol"
p.legend.border_line_width = 3
p.legend.border_line_color = "black"
p.legend.click_policy = "hide"

show(p)

# Basic mean - variance analysis
#log_return
for i in range(1,10):
    SP500['pct_change', column_header[i][1] ] = SP500.iloc[:,i].pct_change()
for i in range(1, 10):
    SP500['log_ret', column_header[i][1]] = np.log(SP500.iloc[:,i]) - np.log(SP500.iloc[:,i].shift(1))


#Average_Price
n1 = 10
for i in range(1,10):
    SP500['cumvol', column_header[i][1]] = SP500.iloc[:,n1].cumsum()
    n1 += 1
for i in range(1,10):
    SP500["WMA Price", column_header[i][1]] = SP500.iloc[0:1, i]

n2 = 10
n3 = 73
n4 = 82
n5 = 1
for n in range(1,10):
    for i in range(1,len(SP500)):
        if SP500.iloc[i, n2] == 0:
            # take previous row value
            SP500.iloc[i, n4] = SP500.iloc[i-1, n4]
        elif SP500.iloc[i, n2] > 0:
            # calculate new average
            SP500.iloc[i, n4] = ((SP500.iloc[i-1, n3]*SP500.iloc[i-1, n4]) + (SP500.iloc[i, n2]*SP500.iloc[i, n5])) / (SP500.iloc[i, n3])
        elif (SP500.iloc[i, n2] < 0) & (SP500.iloc[i, n3] > 0):
            # take previous row value
            SP500.iloc[i, n4] = SP500.iloc[i-1, n4]
        else:
            # vol < 0 and cumsum = 0
            SP500.iloc[i, n4] = 0
    n2 += 1
    n3 += 1
    n4 += 1
    n5 += 1

print(SP500)
print(abs(max(SP500.iloc[:,1])))


