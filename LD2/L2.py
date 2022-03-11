import random
import os
import pandas as pd
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

#   1
with open('tickers.txt') as f:
    lines = f.read().splitlines()

#   2
random.seed(2)
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
    aapl_df = ticker.history(start='2012-01-01', end='2017-12-31')
    aapl_df['Close'].plot(title=x)
    plt.show()
    #print(aapl_df)

    #6 Pasižiūrėti informaciją apie kiekvieną kompaniją Yahoo Finance portale.
#Pasirinktos įmonės ['NCBDF', 'PM', 'EA', 'NKE', 'JNJ']
#NCBDF veikia klientų aptarnavimo srityje, organizuoja poilsines veiklas;
#PM gamina tabako gaminius, cigaretes;
#EA veikia komunikacijos srityje, gamina vaizdo žaidimus ir kitas multimedijas;
#NKE veikia klientų aptarnavimo srityje, gamina avalynę;
#JNJ veikia sveikatos sektoriuje, gamina medikamentus, farmaciją;

    #7
#Su kuriuo rinkos indeksu lygintumėte kiekvienos iš šių kompanijų akcijų grąžą?
#NCBDF lyginama su S&P500
#PM lyginama su MSCI, globaliu indeksu
#EA lyginama su S&P500
#NKE lyginama su MSCI, globaliu indeksu
#JNJ lyginama su S&P500 indeksu, kadangi veikia tarptautinėje rinkoje.

#Sukurkite savo darbiniame kataloge katalogą "uzduotis3" ir dviejų pasirinktų kompanijų palyginimo su dviem skirtingais rinkos indeksais
# grafikus išsaugokite šiame kataloge (tą atlikti galima tokiu būdu:
#pav = DataFrame.plot().get_figure()
#pav.savefig(išsaugojimo kelias)).

#Sukuriama direktorija
directory = "uzduotis3"
parent_dir = r"C:\Users\Kompas\Documents\GitHub\Simonai_python"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)

#Pasirenkamos kompanijos HAS ir LMT. HAS lyginama su S&P500, o LMT - su MSCI.
ticker = yf.Ticker('S&P500', 'MSCI')
data = ticker.history(start='2012-01-01', end='2017-12-31')
plt.plot(data)
plt.show()