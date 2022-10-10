guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    action = input('Гость пришел или ушел? ')
    if action == "пришел":
        name_guest = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет, ' + name_guest +'!')
            guests.append(name_guest)
        else:
            print('Прости, ' + name_guest + ', но мест нет.')
    elif action == "ушел":
        name_guest = input('Имя гостя: ')
        guests.remove(name_guest)
    elif action == "Пора спать":
        break
    print()

print('\nВечеринка закончилась, все легли спать.')