from collections.abc import Iterable


class Iterator:
    """
    Класс Итератор
    Attributes:
        stop (int): последнее число последовательности
        number (int): первое число последовательности
    """
    def __init__(self, stop: int) -> None:
        self.stop = stop
        self.number = 1

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> int:
        if self.number > self.stop:
            raise StopIteration
        square = self.number ** 2
        self.number += 1
        return square


def generator(stop: int) -> Iterable[int]:
    """
    Генерирует последовательность квадраты чисел от 1 N
    :param stop: (int) последнее число последовательности (N)
    """
    for number in range(1, stop + 1):
        square = number ** 2
        yield square


max_number = int(input('Введите число N, для генерации последовательности от 1 до N: '))

my_iter = Iterator(max_number)
print('\nС помощью итератора:')
for num in my_iter:
    print(num, end=' ')

print('\nС помощью генератора:')
my_gen = generator(max_number)
for num in my_gen:
    print(num, end=' ')

print('\nС помощью генератораторного выражения:')
GenSquare = (number ** 2 for number in range(1, max_number + 1))
for num in GenSquare:
    print(num, end=' ')
