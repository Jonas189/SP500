
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

# Basic mean - variance analysis

SP500 = pd.read_csv("S&P500.csv", header=[0,1]).sort_index(level=0)
SP500.drop(columns=SP500.columns[0], axis=1, inplace=True)
SP500 = SP500.set_index(["Date"])
#SP500.reset_index(drop=True, inplace=True)
pd.set_option('display.max_columns', None)
SP500.to_csv("S&P5002.csv")
#print(SP500)

f = open('Stock_Count.txt', 'r')
Number_Stocks = (f.read())
#print(("Number Stocks: " + Number_Stocks))

s = open('Stock_Names.txt', 'r')
s1 = (s.read())
#print(s1)
s2 = s1.replace("'", "")
s3 = s2.replace("[", "")
s4 = s3.replace("]", "")
Stock_names = s4.split(",")
print(len(Stock_names))

# Create new Dataframe
SP500_Analysis = pd.DataFrame(Stock_names, columns = ["Stocks"])

#log_return
SP500_Analysis["Log Return"] = ""
for i in range(0,len(Stock_names)):
    SP500_Analysis.iloc[i, 1] = math.log(SP500.iloc[1,i] / SP500.iloc[len(SP500)-1,i])

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


#Histogram SD

c = figure(width=670, height=400, toolbar_location=None,
           title="Normal (Gaussian) Distribution")
bins = np.linspace(SP500_Analysis.iloc[:,3].min(), SP500_Analysis.iloc[:,3].max(), 100)
hist, edges = np.histogram(SP500_Analysis.iloc[:, 3], density=True, bins=bins)
c.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
         fill_color="skyblue", line_color="white",
         legend_label="S&P 500 Stocks")

c.y_range.start = 0
c.xaxis.axis_label = "Standard Deviation"
c.yaxis.axis_label = "Number of Stocks"

show(c)

