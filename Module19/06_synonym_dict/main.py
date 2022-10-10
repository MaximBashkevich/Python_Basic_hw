count_pair = int(input('Введите количество пар слов: '))
nums_lst = ['Первая', 'Вторая', 'Третья', 'Четвертая', 'Пятая', 'Шестая', 'Седьмая']
synonym = dict()
data = []
for i_pair in range(count_pair):
  pair = (input('{} пара: '.format(nums_lst[i_pair]))).lower().split()
  synonym[pair[0]] = pair[1]
  data.append(pair[0])
  data.append(pair[1])

word = input('\nВведите слово: ').lower()
while word not in data:
    print('Такого слова в словаре нет. \nВведите слово: ', end = '')
    word = input().lower()

for i_word in synonym:
    if word == i_word:
        print('Синоним:', synonym[i_word])
    elif word == synonym[i_word]:
        print('Синоним:', i_word)



