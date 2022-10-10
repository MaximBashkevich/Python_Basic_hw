from collections.abc import Iterable


def hofstadter(hof_list: list) -> Iterable:
    """
    Генерация последовательности Q Хофштадтера
    :param hof_list: начало последовательности
    """
    if hof_list == [1, 2]:
        return
    count = 2
    while True:
        new_hof_number = hof_list[count - hof_list[count - 1]] + hof_list[count - hof_list[count - 2]]
        hof_list.append(new_hof_number)
        count += 1
        yield new_hof_number
        if count > 100:
            return


start = [1, 1]
sequence = hofstadter(start)
print(start[0], start[1], end=' ')
for element in sequence:
    print(element, end=' ')
