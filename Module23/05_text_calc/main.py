def overwrite_file(file_name, action):
    with open(file_name, 'r') as text:
        old_data = text.read()
        new_action = input('Введите исправную строку: ') + '\n'
        new_data = old_data.replace(action, new_action)
    with open(file_name, 'w ') as new_text:
        new_text.write(new_data)


def calculator(file_name, data_errors=[]):
    data_symbol = '+-/*^'
    sum_actions = 0
    with open(file_name) as text:
        for action in text:
            if not action in data_errors:
                try:
                    elements = action.split()
                    if not (elements[1] in data_symbol and len(elements[1]) == 1):
                        raise ValueError
                    elif not (elements[0].isdigit() and elements[2].isdigit()):
                            raise ValueError
                    else:
                        if elements[1] == '+':
                            sum_actions += (int(elements[0]) + int(elements[2]))
                        elif elements[1] == '-':
                            sum_actions += (int(elements[0]) - int(elements[2]))
                        elif elements[1] == '*':
                            sum_actions += (int(elements[0]) * int(elements[2]))
                        elif elements[1] == '/':
                            sum_actions += (int(elements[0]) / int(elements[2]))
                        elif elements[1] == '^':
                            sum_actions += (int(elements[0]) ** int(elements[2]))
                except ValueError:
                    question = input(f'Обнаружена ошибка в строке: {action} Хотите исправить?(Да/Нет) ').lower()
                    if question == 'да':
                        overwrite_file(file_name, action)
                        calculator(file_name, data_errors)
                        raise
                    else:
                        data_errors.append(action)
        sum_actions = round(sum_actions, 2)
        return sum_actions


file_name = 'calc.txt'
result = calculator(file_name)
print('Сумма результатов:', result)
