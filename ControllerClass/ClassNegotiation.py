from ConnectAPI.ClassConnectAPI import ControllerAPIConnect

from binance.enums import *
from binance.exceptions import BinanceAPIException

import pandas as pd

class ControllerNegotiation:
    @classmethod
    def compraCripto(self, criptoPar, quantidade):
        client = ControllerAPIConnect.connectStatus()
        try:
            #PEGAR O VALOR DA QUANTIDADE MINIMA
            info = client.get_symbol_info(criptoPar)
            filterMinQty = next((x for x in info['filters'] if x['filterType'] == 'LOT_SIZE'), None)
            minQty = round(float(filterMinQty['minQty']), 2) if filterMinQty else None
            if minQty >= quantidade:
                ordem = client.create_order(symbol=criptoPar, side='SIDE_BUY', type='ORDER_TYPE_MARKET', quantity=0.0001)
                print('Compra Realizada com Sucesso!')
                #return ordem
            else:
                print(f'Investimento Minimo em {criptoPar} Permitido {minQty}')
        except BinanceAPIException as e:
            print('Erro ao realizar essa compra.')
            print(f'Erro: {e.status_code} - {e.message}')
            
    @classmethod
    def vendaCripto(self):
        try:
            #ordem = client.create_order(symbol=self.criptoPar, side='SIDE_SELL', type='ORDER_TYPE_MARKET', quantity=0.0001)
            print('Venda Realizada com Sucesso!')
        except BinanceAPIException as e:
            print('Erro ao realizar essa venda.')
            print(f'Erro: {e.status_code} - {e.message}')

   
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