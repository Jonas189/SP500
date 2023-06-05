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
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# Basic mean - variance analysis

SP500 = pd.read_csv("S&P500.csv", header=[0,1]).sort_index(level=0)
SP500.drop(columns=SP500.columns[0], axis=1, inplace=True)
SP500 = SP500.set_index(["Date"])
#SP500.reset_index(drop=True, inplace=True)
pd.set_option('display.max_columns', None)

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
s5 = s4.replace(" ", "")
Stock_names = s5.split(",")
print(len(Stock_names))

column_header = (list(SP500.columns))
print(column_header[-1][1])
# Create new Dataframe
SP500_Analysis = pd.DataFrame(Stock_names, columns = ["Stocks"])

for i in range(0,len(Stock_names)):
    SP500['pct_change', column_header[i][1] ] = SP500.iloc[:,i].pct_change()
for i in range(0,len(Stock_names)):
    SP500['log_ret', column_header[i][1]] = np.log(SP500.iloc[:,i]) - np.log(SP500.iloc[:,i].shift(1))

#print(SP500)



#print(x)


test = pd.DataFrame()
test["pct_change"] = ""
test["pct_change_SP500"] = ""
test["pct_change"] = SP500["pct_change", column_header[1][1]].copy()
test["pct_change_SP500"] = SP500["pct_change", column_header[-1][1]].copy()
#print(test)


SP500.to_csv('S&P500:CAPM.csv')


test.drop(index=test.index[0], axis=0, inplace=True)
test.to_csv('test.csv')

x = test["pct_change"]
y = test["pct_change_SP500"]

cov_xy = np.cov(x, y)[1, 0]
var_x = np.var(x, ddof=1)
x_bar = np.mean(x)
y_bar = np.mean(y)

reg = smf.ols(formula='x ~ y', data=test)
results = reg.fit()
b = results.params
print(f'b: \n{b}\n')

print(results.summary())

plt.figure()
plt.plot("pct_change", "pct_change_SP500", data=test, marker='o',ms=3, linestyle='')
plt.plot(test["pct_change"], results.fittedvalues, color='black', linestyle='-')
plt.grid()
plt.ylabel('salary')
plt.xlabel('roe')
plt.show()

