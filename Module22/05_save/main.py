import os

# def write_file(file_path, text):
#     file = open(file_path, 'w')
#     file.write(text)
#     print('Файл успешно перезаписан!')
#     file = open(file_path, 'r')
#     print('Содержание файла:')
#     for i_line in file:
#         print(i_line)
#     file.close()

def save_text(text):
    my_folders = input('Куда хотите сохранить документ? '
                      'Введите последовательность папок'
                       ' (через пробел):\n').split()
    path = os.path.abspath(os.path.join(os.path.sep, *my_folders))
    if os.path.exists(path):
        file_name = input('Введите имя файла: ')
        file_path = file_name + '.txt'
        path = os.path.join(path, file_path)
        if os.path.exists(path):
            answer = input('Вы действительно хотите перезаписать файл? ').lower()
            if answer == 'да':
                file = open(path, 'w')
                file.write(text)
                print('Файл успешно перезаписан!')
                file = open(path, 'r')
                print('\nСодержание файла:')
                for i_line in file:
                    print(i_line)
                file.close()
            else:
                return 0
        else:
            file = open(path, 'w')
            file.write(text)
            print('Файл успешно сохранен!')
            file = open(path, 'r')
            print('\nСодержание файла:')
            for i_line in file:
                print(i_line)
            file.close()
    else:
        print('Путь не найден')


text = input('Введите текст: ')
save_text(text)
