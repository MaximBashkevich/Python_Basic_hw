def site_generator(data, number):
  while number > 0:
    name = input('Введите название продукта для нового сайта: ')
    data['html']['head']['title'] = 'Куплю/продам ' + name + ' недорого'
    data['html']['body']['h2'] = 'У нас самая низкая цена на ' + name
    print(site)
    return site_generator(data, number - 1)


site = {
    'html': {
        'head': {
            'title': ''
        },
        'body': {
            'h2': '',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

count_site = int(input('Сколько сайтов: '))
site_generator(site, count_site)