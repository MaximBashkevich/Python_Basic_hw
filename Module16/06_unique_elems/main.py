first_list = []
second_list = []
sum_list = []
for i in range(3):
    num = int(input('Введите ' + str(i + 1) + '-е число для первого списка: '))
    first_list.append(num)
    sum_list.append(num)
for i in range(7):
    num = int(input('Введите ' + str(i + 1) + '-е число для второго списка: '))
    second_list.append(num)

#sum_list.extend(second_list)
#print(first_list)
#print(second_list)
#print(sum_list)

for index_num in first_list:
    while sum_list.count(index_num) >= 2:
        sum_list.remove(index_num)
        #sum_list.remove(index_num)
        #print(sum_list)
        #for i_count in range(sum_list.count(index_num)):
           # sum_list.remove(index_num)
print('Новый первый список с уникальными элементами:', sum_list)

