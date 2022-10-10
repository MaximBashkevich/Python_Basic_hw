from typing import Iterable
import math


print(*filter(lambda n: (math.factorial(n - 1) + 1) % n == 0, range(2, 1000)))


def prime_numbers() -> Iterable:
    for number in range(1, 1001):
        count = 0
        for divider in range(1, number + 1):
            if number % divider == 0:
                count += 1
        if count == 2:
            yield number


for number in prime_numbers():
    print(number, end=' ')