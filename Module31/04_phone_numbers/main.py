import re
from typing import List


def check_number_phone(numbers_phone: List[str]) -> None:
    """
    Функция для проверки формата номера телефона
    :param numbers_phone: список номеров (List[str])
    """
    pattern = r'[89]\d{9}'
    for index, number in enumerate(numbers_phone):
        check = re.fullmatch(pattern, number)
        if check:
            print('{}-й номер {}: все в порядке'.format(index + 1, number))
        else:
            print('{}-й номер {}: не подходит'.format(index + 1, number))


check_number_phone(['9999999999', '999999-999', '99999x9999', '999999999'])
