from ControllerClass.ClassConnectAPI import ControllerAPIConnect

from binance.enums import *
import pandas as pd

class ControllerNegotiation:
    @classmethod
    def compraCripto(self, criptoPar, quantidade):
        client = ControllerAPIConnect.connectStatus()
        #ordem = client.create_order(symbol=criptoPar, side='SIDE_BUY', type='ORDER_TYPE_MARKET', quantity=0.0001)
        print('Compra Realizada com Sucesso!')
    
    @classmethod
    def vendaCripto(self):
        print('Venda Realizada com Sucesso!')

   
#ORIGIAL
'''
        df = self.tabela()
        compra = False
        # ESTRATÉGIA DE COMPRA E VENDA
        acumulados = (df.Open.pct_change() +1).cumprod() -1
        if not compra:
            if acumulados.iloc[-1] < -0.002:
                #ordem = client.create_order(symbol=self.criptoPar, side='SIDE_BUY', type='ORDER_TYPE_MARKET', quantity=0.0001)
                print('Compra Realizada com Sucesso!')
                compra = True
            else:
                print('Sem Ordens nos últimos 30 minutos')

        if compra:
            while True:
                df = self.tabela(2, ["date_open", "Open"])

#                ordem_executada = df.loc[df.index > pd.to_datetime(ordem['transactTime'], unit='ms')]
 
                if len(ordem_executada) > 0:
                    retorno_ordem_executada = (df.Open.pct_change() + 1).cumprod() -1
                    retorno_ordem_executada[-1] > 0.0015 or retorno_ordem_executada[-1] > -0.0015
                    ordem = client.create_order(symbol=self.criptoPar, side='SIDE_SELL', type='ORDER_TYPE_MARKET', quantity=0.0001)
                    print('Venda Realizada com Sucesso!')
                    break
'''