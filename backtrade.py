from datetime import datetime
import backtrader as bt

class SmaSignal(bt.Signal):

	params = (('period', 20), )

	def __init__(self):

		self.lines.signal = self.data - bt.ind.SMA(period=self.p.period)


#Extraer data de un valor

data = bt.feeds.YahooFinanceData(dataname='ETH-USD', fromdate=datetime(2020, 3, 1), todate=datetime(2020, 7, 1))


cerebro = bt.Cerebro(stdstats = False)
cerebro.adddata(data)

cerebro.broker.setcash(1000.0)
cerebro.add_signal(bt.SIGNAL_LONG, SmaSignal)
cerebro.addobserver(bt.observers.BuySell)
cerebro.addobserver(bt.observers.Value)

#Print antes y despues de la estrategia

print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')
cerebro.run()
print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')

#Se muestra la grafica con la estrategia creada

cerebro.plot(iplot=True, volume=False)