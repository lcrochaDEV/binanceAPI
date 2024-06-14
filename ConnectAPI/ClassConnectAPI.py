from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
load_dotenv()
import os

class ControllerAPIConnect:

    @classmethod
    def __connectApi(cls):
        try:
            API_KEY_BINANCE = os.getenv("API_KEY")
            API_SECRET_BINANCE = os.getenv("API_SECRET")
            return Client(API_KEY_BINANCE, API_SECRET_BINANCE)
        except BinanceAPIException as e:
            print(f'{e.status_code} - {e.message}')
            print(f'Chave ou senha incorretos em Binance API')

    @staticmethod
    def connectStatus(msg=False):
        client = ControllerAPIConnect.__connectApi()
        status = client.get_system_status()
        while True: 
            if status['status'] == 0:
                if msg == True:
                    print(f'Conexão à API e status: {status["msg"]}')
                return client
            else:
                print(f'Sem conexão com Binance API')
                continue

            
#ENVIO DE DADOS PARA API DO TELEGRAM PEDINDO TROCA DE IP