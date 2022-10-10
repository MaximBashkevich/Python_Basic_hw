import random
lst =[random.randint(0, 10) for _ in range(5) for _ in range(2)]
print('Случайный список:', lst)
# Первый способ
new_lst_1 = [(lst[i_num], lst[i_num + 1]) for i_num in range(0, len(lst), 2)]
print('Результат:', new_lst_1)
#Второй способ:
new_lst_2 = []
temp_lst = []
for index, num in enumerate(lst):
  if len(temp_lst) == 2:
    new_lst_2.append(tuple(temp_lst))
    temp_lst = []
    temp_lst.append(num)
  elif index == len(lst) - 1:
    temp_lst.append(num)
    new_lst_2.append(tuple(temp_lst))
  else:
    temp_lst.append(num)
print('Результат:', new_lst_2)