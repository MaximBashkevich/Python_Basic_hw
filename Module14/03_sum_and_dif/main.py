def sum_num(N):
    sum = 0
    while N > 0:
        sum += N % 10
        N //= 10
    return sum

def count_num(N):
    count = 0
    while N > 0:
        count += 1
        N //= 10
    return count


N = int(input('Введите число: '))
sum = sum_num(N)
count = count_num(N)
print('\nСумма чисел:', sum)
print('Количество цифр в числе:', count)
print('Разность суммы и количества цифр:', sum - count)