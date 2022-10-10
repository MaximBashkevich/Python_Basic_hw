text_lst = (input('Введите строку: ')).split()

max_width = 0
big_word = ''
for i_word in text_lst:
    if len(i_word) > max_width:
        big_word = i_word
        max_width = len(i_word)

print('Самое длинное слово:', big_word)
print('Длина этого слова:', max_width)
