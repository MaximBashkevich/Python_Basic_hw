def check_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as protocol, \
            open('registrations_good.log', 'w', encoding='utf-8') as good_log, \
            open('registrations_bad.log', 'w', encoding='utf-8') as bad_log:
        for i_line in protocol:
            user = i_line.split()
            try:
                if len(user) != 3:
                    raise IndexError
                for symbol in user[0]:
                    if not symbol.isalpha():
                        raise NameError
                if not ('.' and '@' in user[1]):
                    raise SyntaxError
                if (int(user[2]) > 99 or int(user[2]) <10):
                    raise ValueError
            except IndexError:
                bad_log.write(f'{i_line[:len(i_line) - 1]}     НЕ присутствуют все три поля/Полей больше чем три\n\n')
            except NameError:
                bad_log.write(f'{i_line[:len(i_line) - 1]}     Поле {user[0]} содержит НЕ только буквы\n\n')
            except SyntaxError:
                bad_log.write(f'{i_line[:len(i_line) - 1]}     Поле {user[1]} НЕ содержит @ и .(точку)\n\n')
            except ValueError:
                bad_log.write(f'{i_line[:len(i_line) - 1]}     Поле {user[2]} НЕ является числом от 10 до 99\n\n')
            else:
                good_log.write(i_line + '\n')


registrations_file = 'registrations.txt'
check_data(registrations_file)
