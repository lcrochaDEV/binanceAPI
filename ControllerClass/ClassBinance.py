from binance.client import Client
from ControllerClass.ClassConnectAPI import ControllerAPIConnect
from datetime import datetime

class ControllerBinance:
    def __init__(self, criptoName, criptoPar):
        self.criptoName = criptoName
        self.criptoPar = criptoPar

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
        client = ControllerAPIConnect.connectStatus()       
        # EXTRATO DE SALDO DO ATIVOS QUE TEMOS EM CONTA
        info = client.get_account()
        lista_ativos = info["balances"]
        for ativos in lista_ativos:
            if float(ativos['free']) > 0:
                print(f"Cripto: {ativos['asset']} Saldo: {ativos['free']}")
    
    @staticmethod
    def saldo_unid(cripto):
        ControllerBinance.data()
        client = ControllerAPIConnect.connectStatus()  
        balance = client.get_asset_balance(asset=cripto)
        print(f"Cripto: {balance['asset']} Saldo: {balance['free']}")

    def verificarDados(self):
        client = ControllerAPIConnect.connectStatus()  
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
                

