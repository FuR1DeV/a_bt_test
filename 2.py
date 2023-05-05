from functools import wraps


#  Создаем функцию декоратора
def cls_method_decorator(param: int):
    #  Определяем функцию декоратора, которая принимает метод в качестве аргумента
    def decorator(func):
        #  Функция-оболочка, которая заменит исходный метод
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            #  Вызываем метод increment_var экземпляра с заданным параметром
            self.increment_var(param)
            #  Вызываем исходный метод с его аргументами и вернём его результат
            return func(self, *args, **kwargs)
        #  Возвращаем функцию-оболочку в качестве нового метода
        return wrapper
    #  Возвращаем функцию декоратора
    return decorator


class SomeClass:
    some_var: int

    def __init__(self, some_var: int):
        self.some_var = some_var

    def increment_var(self, increment: int):
        self.some_var += increment

    @cls_method_decorator(param=30)
    def some_func(self, condition=None):
        print(self.some_var)

    def print_var(self):
        print(self.some_var)

    """
    Вам дан класс SomeClass, содержащий целочисленную переменную some_var
    У него есть вспомогательный метод 'increment_var', 
    увеличивающий значение данной переменной (some_var) на указанную величину
    Ваша задача заключается в том, чтобы реализовать декоратор (cls_method_decorator) 
    Внутри он должен модифицировать some_var через вызов increment_var 
    с указанным декоратору значением
    """


if __name__ == '__main__':
    cls = SomeClass(20)
    cls.print_var()

    cls.some_func()
