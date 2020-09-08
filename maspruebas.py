import pandas as pd
import numpy as np
import yfinance as yf

import cufflinks as cf
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()


df_twtr = yf.download('TWTR',
start='2018-01-01',
end='2018-12-31',
progress=False,
auto_adjust=True)

qf = cf.QuantFig(df_twtr, title="Twitter's Stock Price",
legend='top', name='TWTR')

qf.add_volume()
qf.add_sma(periods=20, column='Close', color='red')
qf.add_ema(periods=20, color='green')

qf.iplot()

