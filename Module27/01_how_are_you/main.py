import functools
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, спрашивает "Как дела?",
    перед запуском декорируемой функции
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        answer = input('Привет! Как дела? ')
        print('А у меня не очень!')
        func(*args, **kwargs)
    return wrapper


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()
