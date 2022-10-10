count_members = int(input('Кол-во человек: '))
members_list = list(range(1, count_members + 1))

loser_num = int(input('Какое число в считалке? '))
print('Значит выбывает каждый ' + str(loser_num) + '-й игрок')


start = 0
while len(members_list) != 1:
    print('\nТекущий круг людей:', members_list)
    print('Начало счёта с номера', members_list[start])
    loser = (loser_num - start) % len(members_list)
    print('Выбывает человек под номером', members_list[loser - 1])
    members_list.remove(members_list[loser - 1])
    start = loser

print('\nОстался человек под номером', members_list[0])