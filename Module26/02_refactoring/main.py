from collections.abc import Iterable


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break


def find_pair(list_1: list, list_2: list, to_find: int) -> Iterable[tuple]:
    """
    Поиск двух чисел из списка, произведение которых равно искомому значению
    :param list_1: первая последовательность
    :param list_2: вторая последовательность
    :param to_find: искомое произведение
    """
    for first_number in list_1:
        for second_number in list_2:
            if first_number * second_number == to_find:
                yield first_number, second_number
                return


print('\nРезультат найден:')
result = find_pair(list_1, list_2, to_find)
for pair in result:
    print(pair[0], '*', pair[1], '=', to_find)
