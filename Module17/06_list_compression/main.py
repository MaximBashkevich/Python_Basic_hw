import random

N = int(input('Количество чисел в списке: '))
first_list = [random.randint(0, 2) for _ in range(N)]
print('Список до сжатия:', first_list)
compression_list = [i_num for i_num in first_list if i_num != 0]
print('Список после сжатия:', compression_list)