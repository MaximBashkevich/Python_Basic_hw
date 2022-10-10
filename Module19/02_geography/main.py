def check_city(city, map_dict):
    for country in map_dict.keys():
        if city in map_dict[country]:
            print('Город {0} расположен в стране {1}'.format(
                city,
                country
            ))
        else:
            print('По городу {} данных нет'.format(city))

count_country = int(input('Количество стран: '))
map_dict = {}
nums_lst_1 = ['Первая', 'Вторая', 'Третья', 'Четвертая', 'Пятая']
nums_lst_2 = ['Первый', 'Второй', 'Третий']
for country in range(count_country):
    map_lst = (input('{} страна: '.format(nums_lst_1[country]))).split()
    map_dict[map_lst[0]] = map_lst[1:]

for i in range(3):
    city = input('\n{} город: '.format(nums_lst_2[i]))
    check_city(city, map_dict)