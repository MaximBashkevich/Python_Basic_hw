import datetime


def input_user(file, user_name):
    with open(file, 'a', encoding='utf-8') as write_file:
        while True:
            try:
                answer = input('Выберите действие('
                               '1- Посмотреть текущий текст чата/'
                               '2 - Отправить сообщение) ')
                if answer == '1':
                    with open(file, 'r', encoding='utf-8') as data_file:
                        for message in data_file:
                            print(message)
                        data_file.close()
                elif answer == '2':
                    with open(file, 'a', encoding='utf-8') as write_file:
                        message = input('Введите сообщение: ')
                        now = datetime.datetime.now()
                        write_file.write(user_name + ': ' + message +
                                         '     ' + now.strftime("%d-%m-%Y  %H:%M")
                                         + '\n')
                        write_file.close()
                elif answer.lower() == 'q':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Неверный ввод')


def chat(file):
    while True:
        try:
            user_name = input('Введите имя пользователя: ')
            if len(user_name) < 3:
                raise ValueError
            if not user_name.isalpha():
                raise TypeError
        except ValueError:
            print('Ошибка. Имя пользователя не может '
                  'быть меньше трех символов.')
        except TypeError:
            print('Ошибка. Имя пользователя не может '
                  'содержать цифры и знаки препинания.')
        else:
            input_user(file, user_name)


chat('chat.txt')
