count_orders = int(input('Введите количество заказов: '))
nums_lst = ['Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый', 'Шестой', 'Седьмой']
orders_dict = dict()
data = []
for i in range(count_orders):
  order = (input('{} заказ: '.format(nums_lst[i]))).split()
  if order[0] in orders_dict:
    if order[1] in orders_dict[order[0]].keys():
      orders_dict[order[0]][order[1]] += int(order[2])
    else:
      orders_dict[order[0]][order[1]] = int(order[2])
  else:
    temp = dict()
    temp[order[1]] = int(order[2])
    orders_dict[order[0]] = temp
print()    
for i_order in orders_dict:
  print(i_order + ':')
  for j_order in orders_dict[i_order]:
    print('\t' + j_order + ':', orders_dict[i_order][j_order])