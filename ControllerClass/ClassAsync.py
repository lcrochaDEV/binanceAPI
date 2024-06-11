import asyncio

class AssyncExec():

    async def __asyncfunction(args):
        await asyncio.gather(*args)  
        pass

    @staticmethod
    def asyncAction(*args):
        try:
            asyncio.run(AssyncExec.__asyncfunction(args))
        except:
            print('Erro ao Executar Ordem')