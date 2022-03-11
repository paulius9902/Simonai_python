import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

print(os.getcwd())
sns.set_style('whitegrid')
ticker_list = ['LMT', 'MSCI']

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
#data_df.index = pd.to_datetime(data_df.index, format='%y%m%d')  # set index as datetime

data_df.plot(figsize=(12,6))
plt.ylabel('Adj Close')
my_path = os.path.dirname(os.path.abspath(__file__))
my_file = r'uzduotis3\graph.png'
plt.savefig(os.path.join(my_path, my_file))
plt.show()
