import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2018, 10, 1)

df = web.DataReader('WTR', 'yahoo', start, end)

df.to_csv('wtr.csv')
df = pd.read_csv('wtr.csv', parse_dates = True, index_col=0)

print(df[['Open', 'High']].head())

df['Adj Close'].plot()
plt.show()

