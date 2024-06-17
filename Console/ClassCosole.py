from ControllerClass.ClassBinance import ControllerBinance
from Console.Decorator import Decorator

cmds = Decorator()

class ControllerCmd(ControllerBinance):
    
    @classmethod
    def menu(self, command):
        @cmds.decorator(command, content_types='data')
        def cmdtData():
            self.data()
        cmdtData()
        @cmds.decorator(command, content_types='saldo')
        def cmdtSaldo():
            self.saldo()
        cmdtSaldo()
        pass


    @classmethod
    def cmd(self, consoleName='Trade CLI'):
        consoleName = 'Trade CLI'
        while True:
            try:
                command = input(f'{consoleName}:').lower()
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


