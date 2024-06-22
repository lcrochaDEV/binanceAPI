from ControllerClass.ClassBinance import ControllerBinance
from Mensagem.ClassInfo import ControllerInfo
from Console.Decorator import *
import lista_criptos

class ControllerCmd(ControllerBinance):
    
    @classmethod
    def menu(self, command):
        @Decorator.decorator(command, content_types='data')
        def cmdtData():
            self.data()
        cmdtData()

        @Decorator.decorator(command, content_types='saldo')
        def cmdtSaldo():
            self.saldo()
        cmdtSaldo()

        @Decorator.decorator(command, content_types='USDT')
        def cmdtSaldoUnidade():
            print(command)
            pass
        cmdtSaldoUnidade()
            #print(next(x for x in lista_criptos.cripto if x == command))

        @Decorator.decorator(command, content_types='saldounidade')
        def submenu():
           self.submenu('Trade CLI>CRIPTO: ')  
        submenu()

    @classmethod
    def cmd(self, consoleName='Trade CLI: '):
        while True:
            try:
                command = input(f'{consoleName}').lower()
                if command != 'exit' and command != 'end':               
                    self.menu(command)
                    pass
                else:
                    break
            except ValueError:
                print('ERRO: Digite um Comando valido', end="\n\n")
            except KeyboardInterrupt:
                print(f'\n{consoleName} Finalizado!')
                break
            finally:
                print('...')


    @classmethod
    def submenu(self, consoleName='Trade CLI: '):
        while True:    
            try:   
                cripto = input(f'{consoleName}').lower()
                if cripto != 'exit' and cripto != 'end':
                    self.menu(cripto)
                    pass
                else:
                    break
            except ValueError: 
                print('ERRO: Digite um Comando valido', end="\n\n")


'''
        
        @Decorator.decorator(command, content_types='saldounidade')
        def cmdtSaldoUnidade():
            while True:    
                try:   
                    cripto = input(f'Trade CLI>CRIPTO: ').lower()
                    if cripto != 'exit' and cripto != 'end':
                        self.saldo_unid(cripto.lower())
                    else:
                        break
                except ValueError:
                    print('ERRO: Digite um Comando valido', end="\n\n")
        cmdtSaldoUnidade()

'''