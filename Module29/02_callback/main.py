from typing import Callable
import functools


app = dict()


def callback(key: str) -> Callable:
    def wrapper(func: Callable):
        app[key] = func

        @functools.wraps(func)
        def wrapped(*args, **kwarg):
            result = func(*args, **kwarg)
            return result

        return wrapped
    return wrapper


@callback('//')
def example():
    print('На сервере что-то происходит...')
    return 'OK'


route = app.get('//')
for _ in range(2):
    if route:
        response = route()
        print('Ответ:', response)
    else:
        print('Такого пути нет')
