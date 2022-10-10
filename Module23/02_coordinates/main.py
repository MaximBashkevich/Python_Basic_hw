import random


def f(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        division = round(x / y, 2)
    except ZeroDivisionError:
        print("Ошибка в функции №1. "
              "Делитель оказался равным 0.")
    else:
        return division


def f2(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        division = round(y / x, 2)
    except ZeroDivisionError:
        print("Ошибка в функции №2. "
              "Делитель оказался равным 0.")
    else:
        return division


with open('coordinates.txt', 'r') as file:
    try:
        for line in file:
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            file_2 = open('result.txt', 'a')
            my_list = sorted([res1, res2, number])
            numbers = []
            for element in my_list:
                numbers.append(str(element))
            numbers.append('\n')
            numbers = ' '.join(numbers)
            file_2.write(numbers)
    except TypeError:
        print("Что-то пошло не так")
