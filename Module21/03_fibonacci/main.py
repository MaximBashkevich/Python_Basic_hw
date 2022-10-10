def fibonacci_number(position):
    if position in (1, 2):
        return 1
    else:
        return fibonacci_number(position - 1) + fibonacci_number(position - 2)


position = int(input('Введите позицию числа в ряде Фибоначчи: '))
number = fibonacci_number(position)
print('Результат:', number)
