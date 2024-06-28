from ControllerClass.ClassBinance import ControllerBinance
from ControllerClass.ClassEstrategia import ControllerEstrategia
from ControllerClass.ClassAsync import AssyncExec
from Mensagem.ClassInfo import ControllerInfo
from Console.ClassCosole import ControllerCmd

#ControllerBinance.tabela("ETHUSDT", Screem=True)
#ControllerBinance.tabela("BTCUSDT", Screem=True)
#ControllerBinance.tabela("NOTUSDT", Screem=True)

AssyncExec.asyncAction(
    #ControllerEstrategia.ordensCompra("NOTUSDT", 0),
    #ControllerEstrategia.ordensCompra("CVXUSDT", 0),
    ControllerEstrategia.ordensCompra("BTCUSDT", 0),
    #ControllerEstrategia.ordensCompra("BETAUSDT", 0),
)


#porcentagem value-((porcent/100)*value)
#5 = 6.900

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
#if __name__ == '__main__':
#    ControllerCmd.cmd()

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