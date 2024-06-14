class ControllerInfo:
        
    @staticmethod
    def infoTab():
        print('#MOSTRA UMA TABELA')
        print('def tabela(self, start_str = "3m", end_str = "30m", numb_colunas=6, listArray = ["date_open", "Open", "High", "Low", "Close", "Volume"], Screem = False):')
        print('    start_str = tempo inicio.')
        print('    end_str = tempo fim.')
        print('    numb_colunas = numero de colunas da tabela.')
        print('    listArray = um array que contem os nomes dos campos de uma tabela.')
        print('    Screem = para exibir/ocultar na tela.', end='\n\n')
    def infoSimbol():
        print('def simbolName(self, msg=False):')
        print('    msg = mostra/oculta mensagem na tela.', end='\n\n')
    def infoSaldo():
        print('def saldo_unid(cripto):')
        print('cripto = nome da cripto.')
        print('exemplo:')
        print('   def saldo_unid("NOT"):', end='\n\n')
    def infoCompraCripto():
        print('def compraCripto(self, criptoPar, quantidade):') 
        print('criptpar = passa o par de cripoto moeda a ser negociado.') 
        print('   quantidade = valor a ser negociado.', end='\n\n')       
    def infoCalculoValorQuantidade():
        print('def calculoValorQuantidade(self, Screem = False):')
        print('    msg = mostra/oculta mensagem na tela.', end='\n\n')
    def infoConnectStatus():
        print('def connectStatus(msg=False):')
        print('    msg = mostra/oculta mensagem na tela.', end='\n\n')
        
        
        
        pass