people_dict = {
    ('Сидоров', 'Илья'): 8,
    ('Сидорова', 'Мария'): 34,
    ('Сидоров', 'Максим'): 39,
    ('Петров', 'Константин'): 26
}

family = input('Введите фамилию: ').lower()
new_family = {i_name: i_age for i_name, i_age in people_dict.items() for j_name in i_name if family in j_name.lower()}
for i_person, i_age in new_family.items():
    print(i_person[0], i_person[1], i_age)

