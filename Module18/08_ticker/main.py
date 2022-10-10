first_str = input('Введите первую строку: ')
second_str = input('Введите вторую строку: ')
list = []
#new str = ''

if len(first_str) != len(second_str):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    for sym in range(len(second_str) - 1, 0, -1):
        list = []
        list.append(second_str[sym:])
        list.append(second_str[:sym])
        new_str = ''.join(list)
        if new_str == first_str:
            print('Первая строка получается из второй со сдвигом', len(second_str) - sym)
            break
        elif sym == 1:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


