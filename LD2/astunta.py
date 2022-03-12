import glob
import numpy as np
import pandas_datareader as pd
from dominate import document
from dominate.tags import *
import os

photos = glob.glob('uzduotis3\*.png')

with document(title='Photos') as doc:
    h1('Photos')
    for path in photos:
        div(img(src=os.path.basename(path)), _class='photo')


with open(r'uzduotis3\gallery.html', 'w') as f:
    f.write(doc.render())

five_companies = df.sort_values('currentPrice').tail(5)['company'].tolist()
    # sukuriamas dataframe grąžų paskaičiavimui
    df_fivecompanies = pd.DataFrame()
    for c in five_companies:
        df_fivecompanies[c] = wb.DataReader(c, data_source='yahoo', start='2012-01-01', end='2017-12-31')['Adj Close']
    print(df_fivecompanies[c])

    # paskaičiuojamos grąžos
    ret = (df_fivecompanies / df_fivecompanies.shift(1)) - 1
    annual_ret = ret.mean() * 250
    print(str(round(annual_ret * 100, 3)) + " %")

    # Paskaičiuojamos 10 portfelių variantų grąžos

    for x in range(10):
        weights = np.random.random('Adj Close')
        weights /= np.sum(weights)
        returns = np.dot(annual_ret, weights)

    # Atvaizduokite portfelio gražų stulpelinę diagramą (pagalvokite, kokiu būdu išsaugoti portfelio grąžąs)
    # Stulpelinių diagramų braižymo pavyzdys - faile "matplotlib - bar charts.ipynb"