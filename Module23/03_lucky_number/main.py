import random


class MyException(Exception):
    pass


def lucky_number(file_name):
    result = 0
    with open(file_name, 'a') as file_output:
        try:
            while True:
                error_number = random.randint(1, 13)
                if error_number == 13:
                    raise BaseException
                number = int(input('Введите число: '))
                file_output.write(str(number) + '\n')
                result += number
                if result >= 777:
                    print('Вы успешно выполнили условие выхода из цикла!')
                    break
        except ValueError:
            print('Программа сломалась. '
                  'Вы ввели букву/символ вместо числа')
        except MyException:
            print('Вас постигла неудача!')
        finally:
            file_output.close()


file_name = 'out_file.txt'
lucky_number(file_name)
