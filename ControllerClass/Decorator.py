class Decorator:
    @staticmethod
    def DecoratorInput(func):
        def wrapper(self, *args):
            command = input(f'Deseja cancelar estas ordens? Y/N:').lower()
            if command == 'y' or command == 'yes':
                func(self, args)
            else:
                print(f'Executada nova ordem')
        pass
        return wrapper
    