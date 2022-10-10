nums_lst = ['Первая', 'Вторая', 'Третья', 'Четвертая', 'Пятая', 'Шестая', 'Седьмая']
count_man = int(input('Введите количество человек: '))
family_dict = dict()
family_lst = []
for i_man in range(count_man):
    two_man = (input('{0} пара: '.format(nums_lst[i_man]))).split()
    family_dict[two_man[0]] = two_man[1]
    family_lst.append(two_man[0])
    family_lst.append(two_man[1])

level_dict = dict()
family = set(family_lst)
for i_child in family:
    level_parent = 0
    if i_child in family_dict.keys():
        level_parent += 1
        parent = family_dict[i_child]
        while True:
            if parent in family_dict.keys():
                level_parent += 1
                parent = family_dict[parent]
            else:
                break
        level_dict[i_child] = level_parent
    else:
        level_dict[i_child] = 0

print('"Высота" каждого члена семьи: ')
for i_man in sorted(level_dict.keys()):
    print(i_man, level_dict[i_man])