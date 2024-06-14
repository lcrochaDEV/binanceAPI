import asyncio

class AssyncExec:

    @classmethod
    async def __asyncfunction(self, args, kwargs):
        await asyncio.gather(*args, **kwargs)  
        pass

    @classmethod
    def asyncAction(self, *args, **kwargs):
        try:
            asyncio.run(self.__asyncfunction(args, kwargs))
        except:
            print('Erro ao Executar Ordem')