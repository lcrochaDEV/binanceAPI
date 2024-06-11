class ControllerInfo:
        
    @staticmethod
    def infoTab():
        print(f'\
        #MOSTRA UMA TABELA
        def tabela(self, start_str = "3m", end_str = "30m", numb_colunas=6, listArray = ["date_open", "Open", "High", "Low", "Close", "Volume"], Screem = False):
            start_str = tempo inicio.
            end_str = tempo fim.
            numb_colunas = numero de colunas da tabela.
            listArray = um array que contem os nomes dos campos de uma tabela.
            Screem = para exibir/ocultar na tela.      
        ')
    def infoSimbol():
        print(f'\
        def simbolName(self, msg=False):   
            msg = mostra/oculta mensagem na tela.    
        ')
    def infoSaldo():
        print(f'\
        def saldo_unid(cripto):
              cripto = nome da cripto.
              exemplo:
                def saldo_unid("NOT"):
        ')
    def infoCompraCripto():
        print(f'\
        def compraCripto(self, criptoPar, quantidade):
              criptpar = passa o par de cripoto moeda a ser negociado.
              quantidade = valor a ser negociado.       
        ')
        pass
