from ControllerClass.ClassBinance import ControllerBinance
from Mensagem.ClassInfo import ControllerInfo
from Console.Decorator import *
import asyncio
import lista_criptos

class ControllerCmd():

    @classmethod
    def cmd(self, consoleName='Trade CLI', submenu=False):
        while True:
            try:
                if submenu == False:
                    command = input(f'{consoleName}: ').lower()
                    if command != 'exit' and command != 'end':               
                        Cli(consoleName, command)
                        pass
                    else:
                        break
                elif submenu == True:
                    command = input(f'{consoleName}: ').lower()
                    if command != 'exit' and command != 'end':               
                        Cli(consoleName, command, submenu=True)
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


class Cli(ControllerBinance):
    def __init__(self, consolename, command, submenu=False):
        self.consolename = consolename
        self.command = command
        self.submenu = submenu
        self.execMenu()
    
    def execMenu(self):
        if self.submenu == False:
            self.menu()
        else:
            self.submenuCli()

    def menu(self):    
        @Decorator.decorator(self.command, content_types='data')
        def cmdtData():
            self.data()
        cmdtData()

        @Decorator.decorator(self.command, content_types='saldo')
        def cmdtSaldo():
            self.saldo()
        cmdtSaldo()

        @Decorator.decorator(self.command, content_types='saldounidade')
        def submenu():
            ControllerCmd.cmd(f'{self.consolename}>CRIPTO', True)  
        submenu()

    def filterList(self):
        lista = [c for c in lista_criptos.cripto if c.lower() == self.command]
        return lista[0].lower()
    
    def submenuCli(self):
        @Decorator.decorator(self.command, content_types=self.filterList())
        def cmdSaldoUnidade():
            self.saldo_unid(self.command)
        cmdSaldoUnidade()
        pass
    