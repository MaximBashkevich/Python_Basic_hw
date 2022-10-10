text = input('Введите строку: ')
text = text[text.index('h') + 1:]
text = text[::-1]
text = text[text.index('h') + 1:]
print('Развёрнутая последовательность между первым и последним h:', text)