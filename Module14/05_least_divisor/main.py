def min_dev(number):
    for num in range(2, number + 1):
        remainder = number % num
        if remainder == 0:
            break
    return num


number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', min_dev(number))