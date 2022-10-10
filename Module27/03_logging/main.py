import datetime, functools
from typing import Callable


def logging(func: Callable) -> Callable:
    """
    Декоратор, логирует ошибки в декорируемых функциях
    в файл function_errors.log
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            time = datetime.datetime.now()
            with open('function_errors.log', 'a', encoding='utf-8') as errors:
                errors.write(f'Функция: {func.__name__}\tОшибка: {error}\t{time}\n')
                print(error)

    return wrapper


@logging
def division_1(x: int, y: int) -> None:
    x = x / y
    # return x


@logging
def division_2(x: int) -> None:
    x = x / y
    # return x


division_1(1, 0)
division_1(1, 1)
division_2(2)
