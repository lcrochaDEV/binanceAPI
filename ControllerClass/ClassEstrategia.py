from ControllerClass.ClassConnectAPI import ControllerAPIConnect
from ControllerClass.ClassNegotiation import ControllerNegotiation
import pandas as pd
import time

# ESTRATÉGIA
class ControllerEstrategia(ControllerNegotiation):
    def __init__(self, criptoName, criptoPar, quantidade):
        self.criptoName = criptoName
        self.criptoPar = criptoPar
        self.quantidade = quantidade

    # TABELAS 
    def tabela(self, numb_colunas=6, listArray = ["date_open", "Open", "High", "Low", "Close", "Volume"]):
        client = ControllerAPIConnect.connectStatus()
        # PEGAR DADOS
        df = pd.DataFrame(client.get_historical_klines(self.criptoPar, '3m', '30m'))
        df = df.iloc[:,:numb_colunas]
        df.columns = listArray
        df = df.set_index(listArray[0])
        df.index = pd.to_datetime(df.index, unit='ms')
        df = df.astype(float)
        return df
    
    @staticmethod
    def media(criptoPar, df = pd.DataFrame([])):
        if not df.empty:      
            somaItens = sum(df.Open) / len(df.Open)
            print(f'{criptoPar} Média {round(somaItens, 3)}')
        else:
            print('É necessário um DataFrame!')
    
    def __calculoValorQuantidade(self):
        client = ControllerAPIConnect.connectStatus()
        #CALCULO DO VALOR EM USDT CONVETENDO PARA QUANTIDADE EM CRIPTO
        flm_price = client.get_margin_price_index(symbol=self.criptoPar)
        # VALOR EM DOLAR(USDT)
        return round(self.quantidade / float(flm_price['price']), 3)

    def ordensCompra(self):
        # ESTRATÉGIA DE COMPRA E VENDA
        while True:
            # TABELAS 
            df = self.tabela()
            acumulados = (df.Open.pct_change() +1).cumprod() -1
            print(f'{self.criptoPar} {round(acumulados.iloc[-1], 3)}')
            #return round(acumulados.iloc[-1], 3)
            if acumulados.iloc[-1] < -0.002:
                self.compraCripto(self.criptoPar, self.quantidade)
                self.__stop()
                break
            else:
                print('Sem Ordens nos últimos 30 minutos')
                #time.sleep(1800) #30 minutos
                time.sleep(200/1000)

    def __stop(self):
            client = ControllerAPIConnect.connectStatus()
            # ESTRATÉGIA DE COMPRA E VENDA
            while True:  
                # TABELAS 
                df = self.tabela()
                acumulados = (df.Open.pct_change() +1).cumprod() -1
                # CARTEIRA SPOT
                infom = client.get_margin_asset(asset=self.criptoName)
                print(f"{infom['assetFullName']}({infom['assetName']}) em Processamento...\n")
                df = self.tabela(2, ["date_open", "Open"])
                if acumulados.iloc[-1] > 0.006 or acumulados.iloc[-1] > -0.002:
                    print(f'{self.criptoPar} {round(acumulados.iloc[-1], 3)}')
                    break

'''                                  
                ordem_executada = df.loc[df.index > pd.to_datetime(ordem['transactTime'], unit='ms')]
 
                if len(ordem_executada) > 0:
                    retorno_ordem_executada = (df.Open.pct_change() + 1).cumprod() -1
                    retorno_ordem_executada[-1] > 0.0015 or retorno_ordem_executada[-1] > -0.0015
                    ordem = client.create_order(symbol=self.criptoPar, side='SIDE_SELL', type='ORDER_TYPE_MARKET', quantity=0.0001)
                    print('Venda Realizada com Sucesso!')
                    break
'''  


'''
    def __menssagem(self):  
        client = ControllerAPIConnect.connectStatus()
        infom = client.get_margin_asset(asset=self.criptoName)
        cont = 4
        for i in range(cont):
            if i < 4: 
                print(f"{infom['assetFullName']}({infom['assetName']}) em Processamento", end="")
                print('.' * i)
            else:
                cont = 0
'''