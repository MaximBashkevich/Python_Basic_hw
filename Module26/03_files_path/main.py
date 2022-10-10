from collections.abc import Iterable


import os


def gen_files_path(path=None) -> Iterable:
    """
    Генерирует пути всех файлов и папок в указанной директории
    :param path: (str/None) директория (по-умолчанию корень диска)
    """
    if path is None:
        path = os.path.abspath(os.path.join('C:/'))
    if os.path.exists(path):
        gen_path = os.walk(path)
        return gen_path
    else:
        raise FileNotFoundError('Указанный путь не найден')


gen_dir = gen_files_path('C:/Users/maxba/OneDrive/Рабочий стол/Python_Basic')
for address, dirs, files in gen_dir:
    for name in files:
        print(os.path.join(address, name))
