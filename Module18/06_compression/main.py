text_lst = list(input('Введите строку: '))
encrypted_text_lst = []
count_sym = 1
text_lst.append('')

for i_sym in range(len(text_lst) - 1):
    if text_lst[i_sym] == text_lst[i_sym + 1]:
        count_sym += 1
    else:
        encrypted_text_lst.append(text_lst[i_sym])
        encrypted_text_lst.append(str(count_sym))
        count_sym = 1

encrypted_text = ''.join(encrypted_text_lst)

print('Закодированная строка: ', encrypted_text)

