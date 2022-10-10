def is_prime(number):
    d = 2
    while number % d != 0 and number > 1:
        d += 1
    return d == number


def crypto(data):
    new_lst = []
    if isinstance(data, (str, list, tuple)):
        for index, value in enumerate(data):
            if is_prime(index):
                new_lst.append(value)
    elif isinstance(data, dict):
        for index, value in enumerate(data):
            if is_prime(index):
                new_lst.append(data[value])
    return new_lst


print(crypto('О Дивный Новый мир!'))