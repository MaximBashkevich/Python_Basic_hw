def add_contact(adressbook):
    person = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    phone = int(input('Введите номер телефона: '))
    adressbook[person] = phone
    return adressbook

def search_contact(adressbook):
    surname = input('Введите фамилию для поиска: ').lower()
    surname_dict = {i_person: i_phone for i_person, i_phone in adressbook.items() for j_person in i_person if
                  surname in j_person.lower()}
    for i_person, i_phone in surname_dict.items():
        print(i_person[0], i_person[1], i_phone)


adressbook = dict()
while True:
    print('\nВведите номер действия:\n'
          '1. Добавить контакт\n'
          '2. Найти человека ')
    action = input()
    if action == '1':
        adressbook = add_contact(adressbook)
        print('Текущий словарь контактов:', adressbook)
    elif action == '2':
        search_contact(adressbook)
    elif action == 'q':
        break
    else:
        print('Неверный ввод!')