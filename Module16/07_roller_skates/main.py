def sort(skates_list):
    temp = 0
    for i_skates in range(len(skates_list)):
        for num in range(len(skates_list)):
            if skates_list[num] > skates_list[i_skates]:
                temp = skates_list[i_skates]
                skates_list[i_skates] = skates_list[num]
                skates_list[num] = temp

    return(skates_list)

skates_list = []
man_size_list = []
count_skates = int(input('Кол-во коньков: '))
for i in range(count_skates):
    skates = int(input('Размер ' + str(i + 1) + '-й пары: '))
    skates_list.append(skates)
skates_list = sort(skates_list)

count_man = int(input('\nКол-во людей: '))
for i in range(count_man):
    size = int(input('Размер ноги ' + str(i + 1) + '-го человека: '))
    man_size_list.append(size)

count_good_size = 0
for i_man in man_size_list:
    for i_skates in skates_list:
        if i_skates >= i_man:
            count_good_size += 1
            skates_list.remove(i_skates)
            break

print('Наибольшее количество людей, которые могут взять ролики:', count_good_size)
