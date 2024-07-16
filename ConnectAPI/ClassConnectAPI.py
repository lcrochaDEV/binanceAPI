from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
load_dotenv()
import os

class ControllerAPIConnect:

    @classmethod
    def __connectApi(self):
        try:
            API_KEY_BINANCE = os.getenv("API_KEY")
            API_SECRET_BINANCE = os.getenv("API_SECRET")
            return Client(API_KEY_BINANCE, API_SECRET_BINANCE)
        except BinanceAPIException as e:
            print(f"\033[33mBinance Error: {e.status_code} - {e.message}'\033[0m")
            print(f"\033[33mChave ou senha incorretos em Binance API\033[0m")

    @classmethod
    def connectStatus(self, msg=False):
        client = self.__connectApi()
        status = client.get_system_status()
        while True: 
            if status['status'] == 0:
                if msg == True:
                    print(f"\033[32mConexão à API e status: {status["msg"]}\033[0m")
                return client
            else:
                print("\033[91mSem conexão com Binance API\033[0m")
                continue

            
#ENVIO DE DADOS PARA API DO TELEGRAM PEDINDO TROCA DE IP