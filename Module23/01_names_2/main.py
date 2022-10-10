class ErrorLengthName(Exception):
    pass


def sum_symbol(file_name):
    line_count = 0
    sum_symbol_name = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as people, open('errors.log', 'w', encoding='utf-8') as errors:
            for i_line in people:
                line_count += 1
                lenght = len(i_line)
                if i_line.endswith('\n'):
                    lenght -= 1
                    try:
                        if lenght < 3:
                            errors.write(f'Ошибка в {line_count} строке файла {file_name}')
                            raise ErrorLengthName
                    except ErrorLengthName:
                        print((f'Ошибка. В строке {line_count} количество символов меньше трёх.'))
                sum_symbol_name += lenght
    except FileNotFoundError:
        print(f'Файла {file_name} не найден')
    print(f'Сумма символов в именах людей в файле {file_name} равна: {sum_symbol_name}')


file_name = 'people.txt'
sum_symbol(file_name)
