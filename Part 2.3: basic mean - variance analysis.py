
# Import Libraries

import numpy as np
import datetime
from datetime import timedelta
import pandas as pd
import yfinance as yf
import requests
import math
from statistics import mean
from bokeh.plotting import figure, show
import matplotlib
from bokeh.models import ColumnDataSource, HoverTool


# Basic mean - variance analysis

SP500 = pd.read_csv("S&P500.csv", header=[0,1]).sort_index(level=0)
SP500.drop(columns=SP500.columns[0], axis=1, inplace=True)
SP500 = SP500.set_index(["Date"])
#SP500.reset_index(drop=True, inplace=True)
pd.set_option('display.max_columns', None)

print(SP500)

f = open('Stock_Count.txt', 'r')
Number_Stocks = (f.read())
#print(("Number Stocks: " + Number_Stocks))

s = open('Stock_Names.txt', 'r')
s1 = (s.read())
#print(s1)
s2 = s1.replace("'", "")
s3 = s2.replace("[", "")
s4 = s3.replace("]", "")
s5 = s4.replace(" ", "")
Stock_names = s5.split(",")
print(len(Stock_names))

# Create new Dataframe
SP500_Analysis = pd.DataFrame(Stock_names, columns = ["Stocks"])


#log_return
SP500_Analysis["Log Return"] = ""
for i in range(0,len(Stock_names)):
    SP500_Analysis.iloc[i, 1] = math.log((SP500.iloc[1,i] / SP500.iloc[len(SP500)-1,i]))

#SMA
SP500_Analysis["Average Price"] = ""
for i in range(0,len(Stock_names)):
    SP500_Analysis.iloc[i, 2] = mean(SP500.iloc[:,i])

#SD
SP500_Analysis["Standard Deviation"] = ""
for i in range(0,len(Stock_names)):
    SP500_Analysis.iloc[i, 3] = np.std(SP500.iloc[:,i])

print(SP500_Analysis.min())
print(SP500_Analysis.max())

# Get Global Industry Classification Standard
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
html = requests.get(url).content
df_list = pd.read_html(html)
Ticker_GICS = df_list[0]
pd.set_option('display.max_columns', None)
Ticker_GICS1 = Ticker_GICS.iloc[:, :3]
Ticker_GICS1 = Ticker_GICS1.rename(columns={"Symbol": "Stocks"})

SP500_Analysis_join = pd.merge(SP500_Analysis, Ticker_GICS1, on ='Stocks', how ='inner')
SP500_Analysis_join.drop("Security", axis =1, inplace = True)

SP500_Analysis_join = SP500_Analysis_join.set_index("Stocks")

grouped = SP500_Analysis_join.groupby("GICS Sector")

GICSlist = SP500_Analysis_join.iloc[:, 3].tolist()
GICSlist = list(dict.fromkeys(GICSlist))
print(GICSlist)
print(len(GICSlist))

Legends = []

list_colors = []
for name in matplotlib.colors.cnames.items():
    list_colors += name

c = 0

tooltips = [
    ("Stock", "@{Stocks}")
]

p = figure(title="Average x SD", x_axis_label='Standard Deviation', y_axis_label='Average', x_range=(0,100), y_range = (0, 400), tools= "hover")
for i in GICSlist:
    p.circle(y=grouped.get_group(i).iloc[:, 1], x=grouped.get_group(i).iloc[:, 2], fill_alpha=1, size=2, legend_label = i, color = list_colors[c])
    c += 10
p.legend.click_policy = "hide"

show(p)

#x_range=(0,100), y_range = (0, 400),

#SP500_Analysis_join.get_group('Health Care')

#print(grouped)
#print(SP500_Analysis_join)





