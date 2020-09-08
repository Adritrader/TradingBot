import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = '0ZSWXPQQ7RKCJL1Q'
ts = TimeSeries(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_intraday(symbol='BTC-USD', interval='15min', outputsize='full') 



period = 60

ti = TechIndicators(key=api_key, output_format='pandas')
data_ti, meta_data_ti = ti.get_sma(symbol='BTC-USD', interval='15min', time_period = '10', series_type = 'close')

df1 = data_ti
df2 = data_ts['4. close'].iloc[10-1::]

df2.index = df1.index

total_df = pd.concat([df1, df2], axis=1)
print(total_df)

total_df.plot()
plt.show()

