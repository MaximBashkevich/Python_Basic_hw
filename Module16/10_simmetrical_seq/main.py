def is_palindrom(num_list):
    if num_list == reverse(num_list):
        return True
    else:
        return False

def reverse(list):
    reverse_list = []
    for num in range(len(list) - 1, -1, -1):
        reverse_list.append(list[num])
    return reverse_list


count_num = int(input('Кол-во чисел: '))
num_list = []
for i in range(count_num):
    num = int(input('Число: '))
    num_list.append(num)
print('\nПоследовательность', num_list)

answer_num_list = []
new_num_list = []
for i_num in range(len(num_list)):

    for j_num in range(i_num, len(num_list)):
        new_num_list.append(num_list[j_num])
    if is_palindrom(new_num_list):
        for i_answer in range(0, i_num):
            answer_num_list.append(num_list[i_answer])
        break
    new_num_list = []

reverse_list = reverse(answer_num_list)


print('Нужно приписать чисел:', len(reverse_list))
print('Сами числа:', reverse_list)