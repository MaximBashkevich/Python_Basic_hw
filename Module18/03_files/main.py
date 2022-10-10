def start(sym):
    check = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
    for i in check:
        if i == sym:
            return True
            break

file_name = input('Имя файла: ')
first_sym = file_name[:1]
if start(first_sym):
    print('Ошибка: название начинается '
          'на один из специальных символов')
elif not file_name.endswith('.txt') or file_name.endswith('.docx'):
    print('Ошибка: неверное расширение '
          'файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')