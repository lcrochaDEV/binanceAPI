from ControllerClass.ClassBinance import ControllerBinance
from ControllerClass.ClassEstrategia import ControllerEstrategia
from Async.ClassAsync import AssyncExec
from Mensagem.ClassInfo import ControllerInfo
from Console.ClassCosole import ControllerCmd
from Websocket.Websocket import WebsocketUsage
import asyncio

#ControllerBinance.tabela("ETHUSDT", Screem=True)
#ControllerBinance.tabela("BTCUSDT", Screem=True)
#ControllerBinance.tabela("NOTUSDT", Screem=True)


while True:
    AssyncExec.asyncAction(
        #ControllerEstrategia.ordensCompra("HARDUSDT", 9000),
        #ControllerEstrategia.ordensCompra("BTCUSDT", 9.000),
        ControllerEstrategia.ordensCompra("RAYUSDT", 9.000),
)

#porcentagem value-((porcent/100)*value)
#5 = 6.900


#ControllerBinance.status_ordes_abertas("BTCUSDT")


#HABILITA O CONSOLE
#if __name__ == '__main__':
#    ControllerCmd.cmd()

#WEBSOCKET
#if __name__ == '__main__':
#    WebsocketUsage.WebsocketUserge()
    

'''
import time 
def stop():
    for i in range(0,5):
        time.sleep(1)
        try:
            command = input(f'Você deseja realizar nova ordem, digite Y/N:') 
            if command == 'y' or command == 'yes':
                print(command)
                break
        except KeyboardInterrupt:
            print('error')
            pass
        finally:
            print('...')

    
stop()
'''


#PEGA 100% DE UM CRIPTO PARA QUALQUER MOÉDA CRIPTO
'''
USDT = client.get_asset_balance(asset="USDT")
print(USDT)
eth_price = client.get_symbol_ticker(symbol="NOTUSDT")
# Calculate how much ETH $200 can buy
buy_quantity = round(float(USDT['free']) / float(eth_price['price']))
print(buy_quantity)
'''

#CALCULO DO VALOR EM USDT CONVETENDO PARA QUANTIDADE EM CRIPTO
'''
# Fetch current price (pseudo-code, replace with actual method to fetch price)
flm_price = client.get_margin_price_index(symbol='BNBUSDT')
# VALOR EM DOLAR(USDT)
quantidade = 9.2336 
# Calculate the quantity of FLM, rounded to 3 decimal places
flm_quantity = round(quantidade / float(flm_price['price']), 3)
print(flm_quantity)
'''


#Colorir termininal
'''
print("\033[94m BLUE \033[0m")
print("\033[32m GREEN \033[0m")
print("\033[33m YELLOW \033[0m")
print("\033[91m RED \033[0m")
 

   1 vermelho = '\033[31m'
   2 verde = '\033[32m'
   3 azul = '\033[34m'
   4 
   5 ciano = '\033[36m'
   6 magenta = '\033[35m'
   7 amarelo = '\033[33m'
   8 preto = '\033[30m'
   9 
  10 branco = '\033[37m'
  11 
  12 restaura cor original = '\033[0;0m'
  13 negrito = '\033[1m'
  14 reverso = '\033[2m'
  15 
  16 fundo preto = '\033[40m'
  17 fundo vermelho = '\033[41m'
  18 fundo verde = '\033[42m'
  19 fundo amarelo = '\033[43m'
  20 fundo azul = '\033[44m'
  21 fundo magenta = '\033[45m'
  22 fundo ciano = '\033[46m'
  23 fundo branco = '\033[47m'
'''