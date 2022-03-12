import random
import os
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import seaborn as sns
import glob
from dominate import document
from dominate.tags import *

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
    price = aapl.info["currentPrice"]
    currentPrice.append(price)
    print(price)

df = pd.DataFrame(list(zip(random_lines, currentPrice)),
               columns =['company', 'currentPrice'])
five_companies = df.sort_values('currentPrice').tail(5)['company'].tolist()
print(five_companies)
for x in five_companies:
    ticker = yf.Ticker(x)
    aapl_df = ticker.history(start='2012-01-01', end='2017-12-31')
    aapl_df['Close'].plot(title=x)
    plt.show()

    #6 Pasižiūrėti informaciją apie kiekvieną kompaniją Yahoo Finance portale.
#Pasirinktos įmonės ['HEN3.DE', 'BMW.DE', 'HAS', 'ML.PA', 'LMT']
#HEN3.DE veikia klientų aptarnavimo srityje, gamina namų apyvokos prekes;
#BMW.DE gamina automobilius, veikia automobilių pramonėje;
#HAS organizuoja pramogines keliones, laisvalaikio veiklas;
#ML.PA gamina automobilių dalis;
#LMT veikia aviacijos svityje;

    #7
#Su kuriuo rinkos indeksu lygintumėte kiekvienos iš šių kompanijų akcijų grąžą?
#HAS lyginama su S&P500 (^GSPC)
#LMT lyginama su MSCI, globaliu indeksu


#Sukurkite savo darbiniame kataloge katalogą "uzduotis3" ir dviejų pasirinktų kompanijų palyginimo su dviem skirtingais rinkos indeksais
# grafikus išsaugokite šiame kataloge (tą atlikti galima tokiu būdu:

#Pasirenkamos kompanijos HAS ir LMT. HAS lyginama su S&P500 (^GSPC), o LMT - su MSCI.
print(os.getcwd())
sns.set_style('whitegrid')
ticker_list = ['LMT', 'MSCI']
ticker_list1 = ['HAS', '^GSPC']

data_df = pd.DataFrame()
for i in range(0, len(ticker_list)):
    ticker = ticker_list[i]
    df_yahoo = yf.download(ticker,
                           start='2012-01-01',
                           end='2017-12-31',
                           progress=False)  # download the data
    data_df = pd.concat([
        data_df,
        df_yahoo['Adj Close']
    ], axis=1)  # store data in one dataframe

data_df.columns = ticker_list  # change columns to ticker name

data_df.plot(figsize=(12,6))
plt.ylabel('Adj Close')
my_path = os.path.dirname(os.path.abspath(__file__))
my_file = r'uzduotis3\graph.png'
plt.savefig(os.path.join(my_path, my_file))
plt.show()

data_df1 = pd.DataFrame()
for i in range(0, len(ticker_list1)):
    ticker1 = ticker_list1[i]
    df_yahoo1 = yf.download(ticker1,
                           start='2012-01-01',
                           end='2017-12-31',
                           progress=False)  # download the data
    data_df1 = pd.concat([
        data_df1,
        df_yahoo1['Adj Close']
    ], axis=1)  # store data in one dataframe

data_df1.columns = ticker_list1  # change columns to ticker name

data_df1.plot(figsize=(12,6))
plt.ylabel('Adj Close')
my_path = os.path.dirname(os.path.abspath(__file__))
my_file = r'uzduotis3\graph.png'
plt.savefig(os.path.join(my_path, my_file))
plt.show()

#8 Tame pačiame kataloge programiškai sukurkite html failą (t.y. tekstinis failas su plėtiniu html) ir į jį įrašykite kodą,
# atvaizduojantį šiuos du grafikus kartu su antrašte ir savo komentarais html puslapyje.

photos = glob.glob('uzduotis3\*.png')

with document(title='Photos') as doc:
    h1('Photos')
    h2('Grafikai')
    for path in photos:
        div(img(src=os.path.basename(path)), _class='photo')


with open(r'uzduotis3\gallery.html', 'w') as f:
    f.write(doc.render())

#9 Apskaičiuokite 5-oje užduotyje atsirinktų kompanijų metines grąžas. Paskaičiuokite N portfelių variantų, sudarytų iš
# šių kompanijų akcijų, grąžas tokiu būdu:

#Pasirinktos įmonės ['HEN3.DE', 'BMW.DE', 'HAS', 'ML.PA', 'LMT']
#Paskaičiuojamos metinės grąžos:

#sukuriamas dataframe grąžų paskaičiavimui
df_fivecompanies = pd.DataFrame()
for c in five_companies:
    df_fivecompanies[c] = wb.DataReader(c, data_source='yahoo', start='2012-01-01', end='2017-12-31')['Adj Close']
print(df_fivecompanies[c])

#paskaičiuojamos grąžos
ret = (df_fivecompanies / df_fivecompanies.shift(1)) - 1
annual_ret = ret.mean() * 250
print(str(round(annual_ret * 100, 3)) + " %")

#Paskaičiuojamos 10 portfelių variantų grąžos
return_list = []
for x in range(10):
    weights = np.random.random(5)
    weights /= np.sum(weights)
    returns = np.dot(annual_ret, weights)
    return_list.append(returns)
    print(return_list)
f = open("returns.txt", "w+")
for i in return_list:
    f.write(str(i) + "\n")
f.close()
with open("returns.txt") as file:
    lines = [line.rstrip() for line in file]

#Atvaizduokite portfelio gražų stulpelinę diagramą (pagalvokite, kokiu būdu išsaugoti portfelio grąžąs)

x_idx = np.arange(len(lines))
plt.bar(x_idx, return_list)
plt.xlabel("Portfelis")
plt.ylabel("Portfelio grąža")
plt.title("Investicinių portfelių grąžos")
my_path = os.path.dirname(os.path.abspath(__file__))
my_file = r'uzduotis3\portfelių_grąžos.png'
plt.savefig(os.path.join(my_path, my_file))
plt.show()