from typing import Callable
import functools


def check_permission(user_name: str) -> Callable:
    """Декоратор для проверяет, достаточно ли прав у пользователя для выполнения действия"""

    def wrap_func(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if user_name != "admin" and func.__name__ == 'delete_site':
                    raise PermissionError
                else:
                    return func(*args, **kwargs)
            except PermissionError:
                print("У пользователя {} нет права доступа на выполнение функции {}". format(
                        user_name, func.__name__
                    ))
            finally:
                return

        return wrapper
    return wrap_func



@check_permission('user_2')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
