def revert(list): #Хотя ,. возм:ожно и нет.
    new_lst = []
    important_sym = '!:.,?;-'
    for word in list:
        new_word = ''
        temp = ''
        temp_s = ''
        for sym in word:
            if sym in important_sym:
                new_word += sym
                temp_s += new_word
                new_word = ''
            else:
                temp = new_word
                new_word = sym + temp
        new_word = temp_s + new_word
        new_lst.append(new_word)
    print('Новое сообщение:', (' '.join(new_lst)))


text_lst = input('Сообщение: ').split()
revert(text_lst)