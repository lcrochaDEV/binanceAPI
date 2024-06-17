from ControllerClass.ClassBinance import ControllerBinance
from ControllerClass.ClassEstrategia import ControllerEstrategia
from ControllerClass.ClassAsync import AssyncExec
from Mensagem.ClassInfo import ControllerInfo
from Console.ClassCosole import ControllerCmd
 

#ControllerBinance.tabela("ETHUSDT", Screem=True)
#ControllerBinance.tabela("BTCUSDT", Screem=True)
#ControllerBinance.tabela("NOTUSDT", Screem=True)

AssyncExec.asyncAction(
    #ControllerEstrategia.ordensCompra("ETHUSDT", 9.2267),
    #ControllerEstrategia.ordensCompra("BTCUSDT", 9.2267),
    #ControllerEstrategia.ordensCompra("NOTUSDT", 9.2267),
)


if __name__ == '__main__':
    ControllerCmd.cmd()

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