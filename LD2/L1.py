import random
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import datetime
import matplotlib.pyplot as plt

#   1
with open('tickers.txt') as f:
    lines = f.read().splitlines()

#   2
random_lines = random.sample(lines, 10)

#   3
for x in random_lines:
    print()
    print("Kompanija: " + x)
    aapl_df = yf.download(x,
                      start='2000-01-01',
                      end=datetime.today(),
                      progress=False,)
    print(aapl_df.head())
    print(aapl_df.info())

    #   4
    ticker = yf.Ticker(x)
    aapl_df['High'].plot(title=x)
    #plt.show()

#   5
currentPrice = []

for x in random_lines:
    print(x)
    aapl = yf.Ticker(x)
    vol = aapl.info["currentPrice"]
    currentPrice.append(vol)
    print(vol)

df = pd.DataFrame(list(zip(random_lines, currentPrice)),
               columns =['company', 'currentPrice'])
five_companies = df.sort_values('currentPrice').tail(5)['company'].tolist()
print(five_companies)
for x in five_companies:
    ticker = yf.Ticker(x)
    aapl_df = ticker.history(period="5y")
    aapl_df['Close'].plot(title=x)
    plt.show()
    #print(aapl_df)