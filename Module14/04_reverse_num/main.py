def invert(num):
    int_num = ''
    float_num = ''
    invert_num = ''
    temp = ''
    flag = False
    for sym in num:
        if sym == '.':
            flag = True
            continue
        if flag == False:
            temp = int_num
            int_num = sym + temp
        else:
            temp = float_num
            float_num = sym + temp
    invert_num = int_num + '.' + float_num
    return invert_num


N = input('Введите первое число: ')
inv_N = invert(N)
K = input('Введите второе число: ')
inv_K = invert(K)

print('\nПервое число наоборот:', inv_N)
print('Второе число наоборот:', inv_K)
sum = float(inv_N) + float(inv_K)
print('Сумма:', sum)