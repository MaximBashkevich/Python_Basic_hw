#text_lst = (input('Введите строку: ')).split()
#new_text_list = []
#new_word = []
#for i_word in text_lst:
#    if i_word[:1].islower():
#        new_word = list(i_word)
#        new_word[0] = new_word[0].upper()
#        word = ''.join(new_word)
#        new_text_list.append(word)
#    else:
#        new_text_list.append(i_word)

#result = ' '.join(new_text_list)
#print('Результат:', result)

text = input('Введите строку: ')
text = text.title()
print('Результат:', text)


