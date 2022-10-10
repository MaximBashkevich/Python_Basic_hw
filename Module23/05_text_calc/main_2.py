def data_control(action):
    data_symbol = ['+', '-', '/', '*', '^', '//', '%']
    elements = action.split()
    try:
        if not (elements[1] in data_symbol and len(elements[1]) == 1):
            raise ValueError
        elif not (elements[0].isdigit() and elements[2].isdigit()):
            raise ValueError
    except ValueError:
        return False
    else:
        return True


def calculator_line(action):
    elements = action.split()
    if elements[1] == '+':
         result = (int(elements[0]) + int(elements[2]))
    elif elements[1] == '-':
        result = (int(elements[0]) - int(elements[2]))
    elif elements[1] == '*':
        result = (int(elements[0]) * int(elements[2]))
    elif elements[1] == '/':
        result = (int(elements[0]) / int(elements[2]))
    elif elements[1] == '^':
        result = (int(elements[0]) ** int(elements[2]))
    elif elements[1] == '//':
        result = (int(elements[0]) // int(elements[2]))
    elif elements[1] == '%':
        result = (int(elements[0]) % int(elements[2]))
    return result


def calculator_file(file_name):
    sum_actions = 0
    with open(file_name) as text:
        for action in text:
            check_action = data_control(action)
            if check_action:
                sum_actions += calculator_line(action)
            else:
                question = input(f'Обнаружена ошибка в строке: {action} Хотите исправить?(Да/Нет) ').lower()
                if question == 'да':
                    new_action = input('Введите исправную строку: ')
                    while True:
                        if data_control(new_action):
                            sum_actions += calculator_line(new_action)
                            break
                        else:
                            new_action = input('Снова ошибка. Введите исправную строку: ')
    print('Сумму результатов:', sum_actions)


file_name = 'calc.txt'
calculator_file(file_name)
