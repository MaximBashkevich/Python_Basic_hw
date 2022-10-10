import functools
import time
from typing import Callable


def sleep(func: Callable) -> Callable:
    """
    Декоратор, делает паузу timeout секунд,
    и запускает декорируемую функции
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper(timeout, *args, **kwargs) -> None:
        print(f'Пауза {timeout} секунд')
        time.sleep(timeout)
        print(f'\nЗапуск программы {func.__name__}')
        func(*args, **kwargs)
    return wrapper


@sleep
def test() -> None:
    print('<Тут что-то происходит...>')


test(timeout=5)
