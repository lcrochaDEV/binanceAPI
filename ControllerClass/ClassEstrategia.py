from ConnectAPI.ClassConnectAPI import ControllerAPIConnect
from ControllerClass.ClassNegotiation import ControllerNegotiation
from ControllerClass.ClassBinance import ControllerBinance

import pandas as pd
import asyncio
import re

client = ControllerAPIConnect.connectStatus()

# ESTRATÉGIA
class ControllerEstrategia(ControllerBinance):
    def __init__(self, criptoPar, quantidade=0):
        self.criptoPar = criptoPar
        self.quantidade = quantidade
     
    @classmethod
    async def ordensCompra(self, criptoPar, quantidade):
        # ESTRATÉGIA DE COMPRA E VENDA
        while True:
            # TABELAS 
            #df = self.tabela(criptoPar)
            #acumulados = ((df.Open.pct_change()).cumprod() +1).cumprod() -1
            #print(f'{criptoPar} {round(acumulados.iloc[-1], 3)}')
            #if acumulados.iloc[-1] > -0.002:
            if await self.__percentual(criptoPar) > -0.002:
                ordem = ControllerNegotiation(criptoPar, quantidade)
                ordem.compraCripto()
                #if ordem == True:
                await self.__ordensVenda(criptoPar, quantidade)
                break
            else: 
                print(f"\033[33m{self.simbolName(criptoPar, True)}Sem Ordens nos últimos 30 minutos\n\033[0m")
                await asyncio.sleep(20)         
                #await asyncio.sleep(1800)
    
    @classmethod
    async def __percentual(self, criptoPar):
        df =  self.tabela(criptoPar)
        #((valor_atual-valor_aterior)/valor_aterior)*100
        print((df.iloc[-1, 3]-df.iloc[-2, 0])/df.iloc[-2, 0]*100)
        print(f'{df.iloc[-2, 0]} {df.iloc[-1, 3]}')
        self.tabela(criptoPar, Screem=True)
        return (df.iloc[-1, 3]-df.iloc[-2, 0])/df.iloc[-2, 0]*100
    
    @classmethod
    async def __ordensVenda(self, criptoPar, quantidade):
        while True:
            await self.__percentual(criptoPar)
            # NOME DA MOEDA
            regexp = re.findall(r"^\w[^US]+|[BRL]+.", criptoPar)[0]
            infom = client.get_margin_asset(asset=regexp)
            if await self.__percentual(criptoPar) < -0.005:
                ordem = ControllerNegotiation(criptoPar, quantidade)
                ordem.vendaCripto()
                break
            else:
                print(f"\033[33m{infom['assetFullName']}({infom['assetName']}) em Processamento...\n\033[0m")
                await asyncio.sleep(20) 
        pass
'''                
'''

'''                                  
            client = ControllerAPIConnect.connectStatus()
            # ESTRATÉGIA DE COMPRA E VENDA
            while True:  
                # TABELAS 
                df = self.tabela(self.criptoPar)
                acumulados = (df.Open.pct_change() +1).cumprod() -1
                # CARTEIRA SPOT
                infom = client.get_margin_asset(asset=self.criptoName)
                #print(f"{infom['assetFullName']}({infom['assetName']}) em Processamento...\n")
                df = self.tabela(2, ["date_open", "Open"])
                
                ordem_executada = df.loc[df.index > pd.to_datetime(ordem['transactTime'], unit='ms')]
 
                if len(ordem_executada) > 0:
                    retorno_ordem_executada = (df.Open.pct_change() + 1).cumprod() -1
                    retorno_ordem_executada[-1] > 0.0015 or retorno_ordem_executada[-1] > -0.0015
                    ordem = client.create_order(symbol=self.criptoPar, side='SIDE_SELL', type='ORDER_TYPE_MARKET', quantity=0.0001)
                    print('Venda Realizada com Sucesso!')
                    break
'''  

