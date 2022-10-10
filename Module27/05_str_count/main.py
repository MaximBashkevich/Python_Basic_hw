import functools
from typing import Callable


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий количество вызовов декорируемой функции
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def test():
    pass


test()
test()

print(test.count)
