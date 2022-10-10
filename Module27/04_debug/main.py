import functools
from typing import Callable


def debug(func: Callable) -> Callable:
    """
    Декоратор, выводит в консоль имя декорируемой функции
    и принимаемые параметры
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        result = func(*args, **kwargs)
        print(f"\nВызывается {func.__name__}(", end='')
        parameters = ', '.join([f'{element}' for element in args] + [f'{key}={val}' for key, val in kwargs.items()])
        print(parameters, end='')
        print(f")\n'{func.__name__}' вернула значение '{result}'")
        print(result)
    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
