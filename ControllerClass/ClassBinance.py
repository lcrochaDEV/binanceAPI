from ConnectAPI.ClassConnectAPI import ControllerAPIConnect
import pandas as pd
from datetime import datetime

client = ControllerAPIConnect.connectStatus()  

class ControllerBinance:
    def __init__(self, criptoName, criptoPar, quantidade=0):
        self.criptoName = criptoName
        self.criptoPar = criptoPar
        self.quantidade = quantidade

    @staticmethod 
    def data():
        client = ControllerAPIConnect.connectStatus()
        #print(Client.get_account_status)
        # TIME DO SERVIDOR BINANCE
        time_res = client.get_server_time()['serverTime']
        server_time = datetime.fromtimestamp(time_res / 1000).strftime('Data/Hora Binance %d/%m/%Y - %HH%M')
        print(f'{server_time}\n')

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
        print(f"Cripto: {balance['asset']} Saldo: {balance['free']}")

    def calculoValorQuantidade(self, Screem = False):
        client = ControllerAPIConnect.connectStatus()
        #CALCULO DO VALOR EM USDT CONVETENDO PARA QUANTIDADE EM CRIPTO
        flm_price = client.get_margin_price_index(symbol=self.criptoPar)
        # VALOR EM DOLAR(USDT)
        if Screem == True:
            print(round(self.quantidade / float(flm_price['price']), 3))
        else:
            return round(self.quantidade / float(flm_price['price']), 3)
            
    def verificarDados(self):
        infom = client.get_margin_asset(asset=self.criptoName)
        infob = client.get_asset_balance(asset=self.criptoName)
        tickers  = client.get_ticker(symbol=self.criptoPar)
        self.data()

        # MERCADO
        print(f"### MERCADO CRIPTO ###\nCRIPTO: {tickers ['symbol']}\nMAIOR PREÇO/24H: {tickers['highPrice']}\nMAIOR MENOR/24H: {tickers['lowPrice']}\nPREÇO ATUAL: {tickers['lastPrice']}\nVOLUME/24H({infom['assetName']}): {tickers['volume']}\nVOLUME/24: {tickers['quoteVolume']}\n")
        # CARTEIRA SPOT
        print(f"CARTEIRA SPOT: {infom['assetFullName']}({infom['assetName']}) VALOR: {infob['free']}\n")

        #res = client.get_historical_klines(self.criptoPar, '3m', '30m')
        print()
    
    # NOME DA MOEDA
    def simbolName(self, msg=False):
        infom = client.get_margin_asset(asset=self.criptoName)
        if msg == False:
            print(f"Dados de {infom['assetFullName']}({infom['assetName']}): ")
        else:
            return f"Dados de {infom['assetFullName']}({infom['assetName']}): "

    # TABELAS
    def tabela(self, start_str = '3m', end_str = '30m', numb_colunas=6, listArray = ["date_open", "Open", "High", "Low", "Close", "Volume"], Screem = False):
        # PEGAR DADOS
        df = pd.DataFrame(client.get_historical_klines(self.criptoPar, start_str, end_str))
        df = df.iloc[:,:numb_colunas]
        df.columns = listArray
        df = df.set_index(listArray[0])
        df.index = pd.to_datetime(df.index, unit='ms')
        df = df.astype(float)
        if Screem == True:
            self.simbolName()
            print(df)
        else:
            return df
    
