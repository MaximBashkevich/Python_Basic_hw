from typing import Callable, Any


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Декоратор, декорирующий декоратор
    :param decorator: (Callable) декоратор
    :return: Callable
    """
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(function_arg1: Any, function_arg2: Any):
        print("Переданные арги и кварги в декоратор:", args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
