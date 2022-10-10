def quantity_price(good, name, store):
    for i_dict in store:
        if i_dict == good:
            quantity = 0
            total_price = 0
            for j_dict in store.get(i_dict):
                quantity += int(j_dict['quantity'])
                total_price += int(j_dict['quantity']) * int(j_dict['price'])
    print('{0} - {1} штук, стоимость {2} рублей'.format(name, quantity, total_price))

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i_good in goods.keys():
  quantity_price (goods[i_good], i_good, store)
