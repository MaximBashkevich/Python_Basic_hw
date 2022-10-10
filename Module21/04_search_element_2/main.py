def search_key(struct, key, depth):
    if depth >= 0:
        if key in struct:
            return struct[key]
        for value in struct.values():
            if isinstance(value, dict):
                depth -= 1
                result = search_key(value, key, depth)
                if result:
                    break
        else:
            result = None
        return result
    else:
        return None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите искомый ключ: ')
question = input('Хотите ввести максимальную'
                 ' глубину? Y/N ').lower()
if question == 'y':
    input_depth = int(input('Введите максимальную глубину: '))
    print('Значение:', search_key(site, key, input_depth))
else:
    print('Значение:', search_key(site, key, 100))
