def same_num(year1, year2):
    for year in range(year1, year2):
        n1 = year // 1000
        n2 = (year // 100) % 10
        n3 = (year // 10) % 10
        n4 = year % 10
        if n1 == n2 == n3 and n1 != n4:
            print(year)
        elif n1 == n2 == n4 and n1 != n3:
            print(year)
        elif n1 == n3 == n4 and n1 != n2:
            print(year)
        elif n2 == n3 == n4 and n1 != n2:
            print(year)

year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))
print('Годы от', year1, 'до', year2, 'с тремя одинаковыми цифрами:')
same_num(year1, year2)