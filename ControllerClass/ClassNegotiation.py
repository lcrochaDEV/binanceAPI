from ConnectAPI.ClassConnectAPI import ControllerAPIConnect
from ControllerClass.ClassBinance import ControllerBinance

from binance.enums import *
from binance.exceptions import BinanceAPIException

client = ControllerAPIConnect.connectStatus()

class ControllerNegotiation(ControllerBinance):
    def __init__(self, criptoPar, quantidade=0):
        self.criptoPar = criptoPar
        self.quantidade = quantidade
     
    def compraCripto(self):
        try:
            #PEGAR O VALOR DA QUANTIDADE MINIMA
            info = client.get_symbol_info(self.criptoPar)
            filterMinQty = next((x for x in info['filters'] if x['filterType'] == 'LOT_SIZE'), None)
            minQty = round(float(filterMinQty['minQty']), 5) if filterMinQty else None
            if minQty <= self.quantidade and self.status_ordes_abertas(self.criptoPar) == []:
                #Teste
                ordem = client.create_test_order(symbol=self.criptoPar, side='BUY', type='MARKET', quantity=self.quantidade)
                #ordem = client.create_order(symbol=self.criptoPar, side='BUY', type='MARKET', quantity=self.quantidade)
                print('\033[32mCompra Realizada com Sucesso!\n\033[0m')
            elif self.status_ordes_abertas(self.criptoPar) != []:
                print(f"\033[33mExitem ordens em aberto.\033[0m")
            else:
                print(f"\033[33mInvestimento Minimo em {self.criptoPar} Permitido {minQty}\033[0m")
        except BinanceAPIException as e:
            print("\033[91mErro ao realizar essa compra.\033[0m")
            print(f"\033[91mBinance Error: {e.status_code} - {e.message}\033[0m")

 
    def vendaCripto(self):
        try:
            ordem = client.create_test_order(symbol=self.criptoPar, side='SELL', type='MARKET', quantity=self.quantidade)
            #ordem = client.create_order(symbol=self.criptoPar, side='SELL', type='MARKET', quantity=self.quantidade)
            print(f"\033[32m{self.simbolName(self.criptoPar, True)}Venda de Realizada com Sucesso!\n\033[0m")

        except BinanceAPIException as e:
            print("\033[91mErro ao realizar essa venda.\033[0m")
            print(f"\033[91mBinance Error: {e.status_code} - {e.message}\033[0m")
