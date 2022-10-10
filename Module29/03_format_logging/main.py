import time
from typing import Callable, Any
import functools


# def timer(func: Callable) -> Callable:
#     """
#     Декоратор- таймер методов класса
#     :param func: (Callable) декорируемый метод
#     :return: (Callable)
#     """
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         finish = round(time.time() - start, 3)
#         print('Завершается метод "{}", время работы = {}s'.format(func.__name__, finish))
#         return result
#     return wrapper


def logged(time_format: str, name_prefix: str = ""):
    """
    Функция для обёртки декоратора log_methods

    :param time_format: формат даты и времени (str)
    :param name_prefix: префикс перед именем функции, для вывода; по умолчанию - '' (str)
    """
    def decorator(func: Callable) -> Callable:
        if hasattr(func, '_logged_decorator') and func._logged_decorator:
            return func

        @functools.wraps(func)
        def decorated_func(*args, **kwargs) -> Any:
            start_time = time.time()
            print("- Запускается '{}'. Дата и время запуска: {} ".format(
                name_prefix + func.__name__,
                time.strftime(time_format)
            ))
            result = func(*args, **kwargs)
            end_time = time.time()
            print("- Завершение '{}', время работы = {:0.3f}s ".format(
                name_prefix + func.__name__,
                end_time - start_time
            ))
            return result
        decorated_func._logged_decorator = True
        return decorated_func
    return decorator


def log_methods(time_format: str) -> Callable:
    """
    Декоратор. Логгирует все методы класса, используя функцию logged.

    :param time_format: формат даты и времени (str)
    """
    def decorator(cls):
        for index_method in dir(cls):
            if index_method.startswith('__'):
                continue
            get_method = getattr(cls, index_method)
            if hasattr(get_method, '__call__'):
                decorated_method = logged(time_format, cls.__name__ + ".")(get_method)
                setattr(cls, index_method, decorated_method)
        return cls
    return decorator


@log_methods("%b %d %Y - %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
