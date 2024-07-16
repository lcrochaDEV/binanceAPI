from ConnectAPI.ClassConnectAPI import ControllerAPIConnect
from ControllerClass.Decorator import *
import pandas as pd
from datetime import datetime

import re
client = ControllerAPIConnect.connectStatus()  

class ControllerBinance:
    @staticmethod 
    def data():
        #print(Client.get_account_status)
        # TIME DO SERVIDOR BINANCE
        time_res = client.get_server_time()['serverTime']
        server_time = datetime.fromtimestamp(time_res / 1000).strftime('Data/Hora Binance %d/%m/%Y - %HH%M')
        print(f"\033[32m{server_time}', end='\n\n\033[0m")

    @staticmethod
    def saldo():   
        # EXTRATO DE SALDO DO ATIVOS QUE TEMOS EM CONTA
        info = client.get_account()
        lista_ativos = info["balances"]
        for ativos in lista_ativos:
            if float(ativos['free']) > 0:
                print(f"Cripto: {ativos['asset']} Saldo: {ativos['free']}")
    
    @staticmethod
    def saldo_unid(cripto):
        ControllerBinance.data()
        balance = client.get_asset_balance(asset=cripto)
        if balance != None:
            print(f"Cripto: {balance['asset']} Saldo: {balance['free']}", end='\n\n')
        else:
            print('Digite um ativo existente.')


    # NOME DA MOEDA
    @classmethod
    def simbolName(self, criptoName=None, Screem = False):
        if criptoName != None:
            regexp = re.findall(r"^\w[^US]+|[BRL]+.", criptoName)[0]
            infom = client.get_margin_asset(asset=regexp)
            if Screem == False:
                print(f"\033[36mDados de {infom['assetFullName']}({infom['assetName']}): \033[0m")
            else:
                return f"Dados de {infom['assetFullName']}({infom['assetName']}): "
            
    # TABELAS
    @classmethod
    def tabela(self, criptoPar, start_str = '3m', end_str = '30m', numb_colunas=6, listArray = ["date_open", "Open", "High", "Low", "Close", "Volume"], Screem = False):
        # PEGAR DADOS
        try:
            df = pd.DataFrame(client.get_historical_klines(criptoPar, start_str, end_str))
            df = df.iloc[:,:numb_colunas]
            df.columns = listArray
            df = df.set_index(listArray[0])
            df.index = pd.to_datetime(df.index, unit='ms')
            df = df.astype(float)
            if Screem == True:
                self.simbolName(criptoPar)
                print(f"\033[36mTabela de Informações {criptoPar} dos Últimos 30 Minutos\033[0m")
                print(f"\033[35m{df}\033[0m")
                acumulados = ((df.Open.pct_change()).cumprod() +1).cumprod() -1
                print(f"\033[36mAcumulados {criptoPar} {round(acumulados.iloc[-1], 3)}\n\033[0m")
            else:
                return df
        except:
            print('Não retornou uma tabela')

    @classmethod   
    def calculoValorQuantidade(self, criptoPar, quantidade, Screem = False):
        #CALCULO DO VALOR EM USDT CONVETENDO PARA QUANTIDADE EM CRIPTO
        flm_price = client.get_margin_price_index(symbol=criptoPar)
        # VALOR EM DOLAR(USDT)
        if Screem == True:
            print(f"{round(quantidade / float(flm_price['price']), 3)}")
        else:
            return round(quantidade / float(flm_price['price']), 3)

    @classmethod        
    def verificarDados(self, criptoPar):
        if criptoPar != None:
            regexp = re.findall(r"^\w[^US]+|[BRL]+.", criptoPar)[0]
            
            infom = client.get_margin_asset(asset=regexp)
            infob = client.get_asset_balance(asset=regexp)
            tickers  = client.get_ticker(symbol=criptoPar)
            self.data()

            # MERCADO
            print(f"### MERCADO CRIPTO ###\nCRIPTO: {tickers ['symbol']}\nMAIOR PREÇO/24H: {tickers['highPrice']}\nMAIOR MENOR/24H: {tickers['lowPrice']}\nPREÇO ATUAL: {tickers['lastPrice']}\nVOLUME/24H({infom['assetName']}): {tickers['volume']}\nVOLUME/24: {tickers['quoteVolume']}\n")
            # CARTEIRA SPOT
            print(f"CARTEIRA SPOT: {infom['assetFullName']}({infom['assetName']}) VALOR: {infob['free']}\n")

            #res = client.get_historical_klines(self.criptoPar, '3m', '30m')
            print()

    @classmethod
    def status_ordes_abertas(self, criptoPar, Screem = False):
        orders = client.get_open_orders(symbol=criptoPar)        
        if Screem == True:
            print(orders)
        else:
            return orders

    @classmethod
    def check_order_status(self, criptoPar, id=0, Screem = False):
        order = client.get_order(symbol=criptoPar, orderId=id)
        if Screem == True:
            print(order)
        else:
            return order


    @classmethod
    @Decorator.DecoratorInput
    def cancel_an_order(self, criptoPar, id=0, Screem = False):
        result = client.cancel_order(symbol=criptoPar, orderId=id, Screem=True)
        print(result)
        if Screem == True:
            print(result)
            print('Ordens canceladas')
        else:
            return result
