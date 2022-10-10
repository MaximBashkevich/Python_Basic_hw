def vower_sym(sym):
    #vower_list = []
    vower = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

    for i_vower in vower:
        if i_vower == sym.lower():
            return sym
            break



text = input('Введите текст: ')
text_2 = vower_sym(text)
new_text = [vower_sym(i_sym) for i_sym in text if vower_sym(i_sym) != None]
print('\nСписок гласных букв:', new_text)
print('Длина списка:', len(new_text))
