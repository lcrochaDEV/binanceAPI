class ControllerInfo:
        
    @staticmethod
    def infoTabela():
        print('#MOSTRA UMA TABELA')
        print('def tabela(self, criptoPar, start_str = "3m", end_str = "30m", numb_colunas=6, listArray = ["date_open", "Open", "High", "Low", "Close", "Volume"], Screem = False):')
        print('    criptoName = é passado o par da cripto moeda')
        print('    start_str = tempo inicio.')
        print('    end_str = tempo fim.')
        print('    numb_colunas = numero de colunas da tabela.')
        print('    listArray = um array que contem os nomes dos campos de uma tabela.')
        print('    Screem = para exibir/ocultar na tela.', end='\n\n')
    def infoSimbolName():
        print('def simbolName(self, criptoName=None, msg=False):')
        print('    criptoName = é passado o par da cripto moeda')
        print('    msg = mostra/oculta mensagem na tela.', end='\n\n')
    def infoSaldo():
        print('def saldo_unid(cripto):')
        print('    cripto = nome da cripto.')
        print('         exemplo:')
        print('         def saldo_unid("NOT"):', end='\n\n')
    def infoCompraCripto():
        print('def compraCripto(self, criptoPar, quantidade=0):') 
        print('   criptpar = passa o par de cripoto moeda a ser negociado.') 
        print('   quantidade = valor a ser negociado.', end='\n\n')       
    def infoCalculoValorQuantidade():
        print('def calculoValorQuantidade(self, criptoPar, quantidade, Screem = False):')
        print('   criptpar = passa o par de cripoto moeda a ser negociado.') 
        print('   quantidade = valor a ser negociado.')       
        print('    msg = mostra/oculta mensagem na tela.', end='\n\n')
    def infoConnectStatus():
        print('def connectStatus(msg=False):')
        print('    msg = mostra/oculta mensagem na tela.', end='\n\n')
    def infoOrdensCompra():
        print('async def ordensCompra(self, criptoPar, quantidade):')
        print('   criptpar = passa o par de cripoto moeda a ser negociado.') 
        print('   quantidade = valor a ser negociado.', end='\n\n')
    def infoVerificarDados():
        print('def verificarDados(self, criptoPar):')    
        print('   criptpar = passa o par de cripoto moeda a ser negociado.', end='\n\n') 
        pass