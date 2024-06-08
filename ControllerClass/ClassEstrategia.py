from ControllerClass.ClassConnectAPI import ControllerAPIConnect
from ControllerClass.ClassNegotiation import ControllerNegotiation
from ControllerClass.ClassBinance import ControllerBinance

import time
import asyncio

# ESTRATÉGIA
class ControllerEstrategia(ControllerBinance):
    def __init__(self, criptoName, criptoPar, quantidade):
        self.criptoName = criptoName
        self.criptoPar = criptoPar
        self.quantidade = quantidade

    async def exec(self):
        await self.__ordensCompra()
    
    async def __ordensCompra(self):
        # ESTRATÉGIA DE COMPRA E VENDA
        while True:
            # TABELAS 
            df = self.tabela()
            acumulados = (df.Open.pct_change() +1).cumprod() -1
            #print(f'{self.criptoPar} {round(acumulados.iloc[-1], 3)}')
            if acumulados.iloc[-1] < -0.002:
                ControllerNegotiation.compraCripto(self.criptoPar, self.quantidade)
                #self.__stop()
                break
            else: 
                print(f'{self.simbolName(True)}Sem Ordens nos últimos 30 minutos')
                await asyncio.sleep(1800)
                #time.sleep(1800) #30 minutos
                #time.sleep(200/1000)
                

    def __stop(self):
            client = ControllerAPIConnect.connectStatus()
            # ESTRATÉGIA DE COMPRA E VENDA
            while True:  
                # TABELAS 
                df = self.tabela()
                acumulados = (df.Open.pct_change() +1).cumprod() -1
                # CARTEIRA SPOT
                infom = client.get_margin_asset(asset=self.criptoName)
                #print(f"{infom['assetFullName']}({infom['assetName']}) em Processamento...\n")
                df = self.tabela(2, ["date_open", "Open"])
'''                                  
                ordem_executada = df.loc[df.index > pd.to_datetime(ordem['transactTime'], unit='ms')]
 
                if len(ordem_executada) > 0:
                    retorno_ordem_executada = (df.Open.pct_change() + 1).cumprod() -1
                    retorno_ordem_executada[-1] > 0.0015 or retorno_ordem_executada[-1] > -0.0015
                    ordem = client.create_order(symbol=self.criptoPar, side='SIDE_SELL', type='ORDER_TYPE_MARKET', quantity=0.0001)
                    print('Venda Realizada com Sucesso!')
                    break
'''  

