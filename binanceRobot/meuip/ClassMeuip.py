import requests

class ControllerIP:
    def __init__(self, site, url, ip):
        self.site = site
        self.url = url
        self.ip = ip

    @staticmethod
    def meuip():
        ip_publico = requests.get('https://api.ipify.org/').text
        print(f'IP Publico: {ip_publico}')
        return ip_publico
    
    @staticmethod
    def trocarIP():
        return "Lucas Você precisa trocar o IP na Binance"
