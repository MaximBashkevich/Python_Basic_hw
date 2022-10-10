menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
print('Доступное меню:', menu)
menu_lst = menu.split(';')
new_menu = ' ,'.join(menu_lst)
print('На данный момент в меню есть:', new_menu)
