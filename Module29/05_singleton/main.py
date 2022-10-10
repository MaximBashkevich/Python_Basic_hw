from typing import Callable


def singleton(cls) -> Callable:
    """
    Декоратор, преобразует класс в класс-синглтон
    :param cls:
    :return:
    """
    def wrapper():
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls, cls).__new__(cls)
        return cls.instance
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()


print(id(my_obj))
print(id(my_another_obj))


print(my_obj is my_another_obj)
