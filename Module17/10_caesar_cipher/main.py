def cezar(sym, shift):
    data = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
    if data.count(sym) != 0:
        position = data.index(sym)
        new_position = position + shift
        if new_position > 31:
            new_position -= 32
        return data[new_position]
    else:
        return sym

text = input('Введите сообщение: ')
text_list = list(text)
shift = int(input('Введите сдвиг: '))
encryption_text = [cezar(i_sym, shift) for i_sym in text_list]

print('Зашифрованное сообщение:', end = ' ')
for i_sym in encryption_text:
    print(i_sym, end = '')