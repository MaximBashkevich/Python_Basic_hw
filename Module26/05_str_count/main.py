from collections.abc import Iterable


import os


def count_string(path: str) -> Iterable[int]:
    """
    Функция-генератор количества строк в питоновских файлахв указанной директории
    """
    path = os.path.abspath(path)
    print('Количество строк кода в папке', path, 'равно: ', end='')
    for address, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.py'):
                count_string = 0
                path = os.path.abspath(os.path.join(address, name))
                with open(path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line != '\n' and line[0] != '#':
                            count_string += 1
                    yield count_string


path = os.path.join('..', '..')
count = count_string(path)
print(sum(count))
