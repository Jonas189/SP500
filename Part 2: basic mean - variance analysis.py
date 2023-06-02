
# Import Libraries

import numpy as np
import datetime
from datetime import timedelta
import pandas as pd
import yfinance as yf
import requests

# Basic mean - variance analysis

SP500 = pd.read_csv("S&P500.csv", header=[0,1]).sort_index(level=0)
SP500.drop(columns=SP500.columns[0], axis=1, inplace=True)
SP500 = SP500.set_index(["Date"])
#SP500.reset_index(drop=True, inplace=True)
pd.set_option('display.max_columns', None)
print(SP500)

f = open('Stock_Count.txt', 'r')
Number_Stocks = (f.read())
print(("Number Stocks: " + Number_Stocks))







