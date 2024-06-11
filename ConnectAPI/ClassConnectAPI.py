from binance.client import Client
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
        except:
            print(f'Sem conexão com a API da Binance')

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
                print(f'Sem conexão com a API da Binance')
                continue

            
#ENVIO DE DADOS PARA API DO TELEGRAM PEDINDO TROCA DE IP