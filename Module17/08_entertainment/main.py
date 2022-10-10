import random

count_stick = int(input('Количество палок: '))
count_throw = int(input('Количество бросков: '))
sticks = ['|' for _ in range(count_stick)]
print(sticks)
for i in range(1, count_throw + 1):
    Left_i = 0
    Right_i = 0
    A = random.randint(1, count_stick)
    B = random.randint(1, count_stick)
    if A > B:
        Right_i = A
        Left_i = B
    else:
        Right_i = B
        Left_i = A

    sticks[Left_i - 1:Right_i] = ['.' for _ in range(Right_i - Left_i + 1)]
    print('Бросок ' + str(i) + '. Сбиты палки с номера', Left_i, 'по номер', Right_i)

for i_stick in sticks:
    print(i_stick, end = '')
