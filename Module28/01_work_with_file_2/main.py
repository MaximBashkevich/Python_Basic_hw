from typing import TextIO
import os


class File:
    def __init__(self, name: str, mode: str) -> None:
        self.name = name
        self.mode = mode
        print('Открываю файл {}\n'.format(name))

    def __enter__(self) -> TextIO:
        # try:
        if not os.path.exists(os.path.join(self.name)) and self.mode == 'r':
            self.new_file = open(self.name, 'w', encoding='utf-8')
            text = input('Файл не найден.'
                         '\nФайл открыт в режиме записи, введите текст: ')
            self.new_file.write(text)
        else:
            self.new_file = open(self.name, self.mode, encoding='utf-8')
        return self.new_file
        # except FileNotFoundError:
        #     print('ОШИБКА. Файл {} не найден'.format(self.name))

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.new_file:
            self.new_file.close()
        return True


with File('example.txt', 'a') as file_1:
    file_1.write('Привет!\n')

with File('exampl.txt', 'r') as file_2:
    print(file_2.read())
