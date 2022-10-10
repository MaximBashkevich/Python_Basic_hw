def is_palindrom(text):
    uneven_syms = 0
    text_set = set(list(text))
    sym_dict = dict()
    for sym in text_set:
        sym_dict[sym] = text.count(sym)
    for i_sym in sym_dict.values():
        if i_sym % 2 == 1:
            uneven_syms += 1
    if uneven_syms > 1:
        print('Нельзя сделать палиндромом')
    else:
        print('Можно сделать палиндромом')


text = input('Введите строку: ')
is_palindrom(text)