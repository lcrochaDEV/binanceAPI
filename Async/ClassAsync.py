import asyncio

class AssyncExec:

    @classmethod
    async def __asyncfunction(self, args=None, kwargs=None):
        try:
            await asyncio.gather(*args, **kwargs)
        except:
            print('Erro ao Executar Ordem')

    @classmethod
    def asyncAction(self, *args, **kwargs):
        asyncio.run(self.__asyncfunction(args, kwargs))


    @staticmethod 
    def decorator(func=None):
        def wrapper(self):
            asyncio.run(func(self))
        pass
        return wrapper