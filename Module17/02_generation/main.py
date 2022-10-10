N = int(input('Введите длину списка: '))
num_list = [(1 if i_num % 2 == 0 else i_num % 5) for i_num in range(N)]
print('Результат:', num_list)
