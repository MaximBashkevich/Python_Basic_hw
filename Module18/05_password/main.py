def check_upper(list):
    for sym in list:
        if sym.isupper():
            return True
            break
    return False

def check_digit(list):
    for sym in list:
        if sym.isdigit():
            return True
            break
    return False


while True:
    password = list(input('Придумайте пароль: '))
    if len(password) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    elif not check_upper(password):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    elif not check_digit(password):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break

