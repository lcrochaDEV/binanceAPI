class Decorator:
    @staticmethod
    def decorator(*args, **kwargs):
        def dec(func=None):
            def wrapper():
                for key, value in kwargs.items():
                    if value == args[0]:
                        print(value)
                        func()
                    pass
            return wrapper
        return dec
