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
from bokeh.palettes import Spectral11

from sklearn.preprocessing import MinMaxScaler

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

# Import Stock random Data from Yahoo

random_ticker = np.random.choice(ticker_as_list, 9, replace=False)
#print(random_ticker)
random_ticker_as_list = random_ticker.tolist()
print(random_ticker_as_list)

start_date = '2020-05-01'
end_date = '2021-05-01'
SP500 = yf.download(random_ticker_as_list, start_date, end_date)
SP500["Date"] = SP500.index
SP500 = SP500[["Date", "Open"]]
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

#SP500_sklearn = SP500.copy()
#SP500_sklearn[column] = MinMaxScaler().fit_transform(np.array(SP500_sklearn[column]).reshape(-1,1))

#print(SP500.tail())

# Visualization
SP500.index = SP500.index.astype(str)
column_header = (list(SP500.columns))
p = figure(title = "S&P500 Example", x_axis_label = 'Time', x_axis_type="datetime", y_axis_label = 'Scaled Prices',width=800, tools = "pan, hover")
p.line(SP500.iloc[:,0], SP500.iloc[:,1], legend_label = str((column_header[1][1])), color ="red", line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,2], legend_label = str((column_header[2][1])), color ="green", line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,3], legend_label = str((column_header[3][1])), color ="blue", line_width = 2)
p.line(SP500.iloc[:,0], SP500.iloc[:,4], legend_label = str((column_header[4][1])), color ="orange", line_width = 2)
#p.line(SP500.iloc[:,0], SP500.iloc[:,5], legend_label = str((column_header[5][1])), line_width = 2)
#p.line(SP500.iloc[:,0], SP500.iloc[:,6], legend_label = str((column_header[6][1])), line_width = 2)
#p.line(SP500.iloc[:,0], SP500.iloc[:,7], legend_label = str((column_header[7][1])), line_width = 2)
#p.line(SP500.iloc[:,0], SP500.iloc[:,8], legend_label = str((column_header[8][1])), line_width = 2)
#p.line(SP500.iloc[:,0], SP500.iloc[:,9], legend_label = str((column_header[9][1])), line_width = 2)
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

print((SP500))







a = (column_header[1][1])
b = SP500.iloc[:,0]
c = SP500.iloc[:,1]

#a_as_list = a.tolist()
b_as_list = b.tolist()
c_as_list = c.tolist()

p.add_tools(HoverTool(
    tooltips=[
        ( 'date',   "b_as_list"),
        ( 'close',  "c_as_list" ), # use @{ } for field names with spaces
    ],

    formatters={
        'date'      : 'datetime', # use 'datetime' formatter for 'date' field
    },

    # display a tooltip whenever the cursor is vertically in line with a glyph
    mode='vline'
))

show(p)

#print(b_as_list)

#n_source = zip(b_as_list, c_as_list)
#new = pd.DataFrame(list(n_source))
#new["Ticker"] = a
#new.columns = ["Date", "Opening_Value", "Ticker"]
#new_right_order = new.iloc[:, [2, 0, 1]]




#b = figure(title = "S&P500 Example", x_axis_label = 'Time', x_axis_type="datetime", y_axis_label = 'Scaled Prices',width=800, tools='hover')
#b.line(concat_df.iloc[:,0], concat_df[:,1], legend_label = str((column_header[1][1])), color ="red", line_width = 2)






#for index in range(len(SP500)):

#new_df = pd.DataFrame(empty_list, columns=["Date", "Name", "Value"])
#print(new_df)


source = ColumnDataSource(data=dict(x=b, y=c))

TOOLTIPS = [
        ("index", "$index"),
        ("Date", "$x"),
        ("Value", "$y"),
]

c = figure(width=400, height=400,
           title="Mouse over the dots", tooltips=TOOLTIPS)
c.line('x', 'y', source=source)

#show(c)


