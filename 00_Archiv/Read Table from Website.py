import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[0]
pd.set_option('display.max_columns', None)
#print(df)
#df.to_csv('my data.csv')

#extract first row
ticker = df["Symbol"]
#print(ticker)
ticker_as_list = ticker.tolist()
print(ticker_as_list)
