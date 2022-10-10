def chech_int(ip_lst):
    flag = True
    for num in ip_lst:
        if not num.isdigit():
            flag = False
            print(num + '- это не целое/положительное число.')
    return flag

def chech_min_max(ip_lst):
    flag = True
    for num in ip_lst:
        if int(num) > 255:
            flag = False
            print(num, 'превышает 255.')
    return flag



while True:
    ip = input('Введите IP-адрес: ')
    ip_lst = ip.split('.')
    if ip.count('.') != 3 and len(ip_lst) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
    elif not chech_int(ip_lst):
        print()
    elif not chech_min_max(ip_lst):
        print()
    else:
        print('IP-адрес корректен.')
        break



