from ControllerClass.ClassBinance import ControllerBinance
from ControllerClass.ClassEstrategia import ControllerEstrategia
import time as time
from ControllerClass.ClassAsync import AssyncExec
   
import asyncio
  
Binance = ControllerBinance("NOT", "NOTUSDT")
Binance.tabela(Screem = True)
NOT = ControllerEstrategia("NOT", "NOTUSDT", 9.2267)

#ControllerBinance.tabela('BTCUSDT')
BTC = ControllerEstrategia("BTC", "BTCUSDT", 9.2267)

#ControllerBinance.tabela('ETHUSDT')
ETH = ControllerEstrategia("ETH", "ETHUSDT", 9.2267)

AssyncExec.asyncAction(
    NOT.exec(), 
    BTC.exec(), 
    ETH.exec(),
)
#AssyncExec.asyncAction(BTC.exec())
#AssyncExec.asyncAction(ETH.exec())


'''
async def order():
    await asyncio.gather(
        NOT.exec(),
        BTC.exec(),
        ETH.exec(),          
    )
asyncio.run(order()) 
'''
'''
if __name__ == '__main__':
    consoleName = 'Trade CLI'
    while True:
        try:
            conole = int(input(f'{consoleName}:'))
        except ValueError:
            print('ERRO: Digite um Comando valido', end="\n\n")
        except KeyboardInterrupt:
            print(f'\n{consoleName} Finalizado!')
            break
        else:
            print('...')
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