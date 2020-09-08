import pandas as pd
import pandas_datareader as pdr
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

plt.style.use('tableau-colorblind10')

def DEMA(accion,dias,n):

	# Parametros de tiempo

	fin = dt.date.today()
	inicio = fin - dt.timedelta(dias)

	# Descarga de la accion y limpieza

	df = pdr.get_data_yahoo(str(accion), start=inicio, end=fin)
	df = df[df['Volume']>0]
	df = df.drop('Adj Close', axis=1)

	#Transforma la escala de precios a formato logaritmico
	

	# Calculo del DEMA

	df['EMA'] = df.iloc[:,3].ewm(span=n).mean() #EMA(n)
	df['EMA_EMA'] = df['EMA'].ewm(span=n).mean() #EMA(EMA(n))
	df['2xEMA'] = np.multiply(2,df['EMA']) # 2 x EMA
	df['DEMA'] = df['2xEMA'] - df['EMA_EMA']

	# Graficar

	plt.figure(figsize=[15,10])
	plt.grid(True)
	plt.title(str(accion) + ' - DEMA')
	plt.plot(df['Close'], label='Precio de cierre', lw='2.5', color='yellow')
	plt.plot(df['DEMA'], color='red', label='Media Movil Exponencial Doble', ls ='--', lw='3')
	plt.xlabel('Fecha')
	plt.ylabel('Precio')
	plt.legend()
	plt.show()
	#print(plt.style.available)

DEMA('ETH-USD', 10, 15)

