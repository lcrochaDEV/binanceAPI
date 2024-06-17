from ConnectAPI.ClassConnectAPI import ControllerAPIConnect

class ControllerMessenger():
    #Menssagem Notcoin(NOT) em Processamento...
    def __menssagem(self):  
        client = ControllerAPIConnect.connectStatus()
        infom = client.get_margin_asset(asset=self.criptoName)
        cont = 4
        print(f"{infom['assetFullName']}({infom['assetName']}) em Processamento")
        for i in range(cont):
            if i < 4: 
                print('.'*i)
            else:
                cont = 0