def tpl_sort(tpl):
    lst = [num for num in tpl]
    flag = True
    for i_num in lst:
       if i_num % 1 != 0:
           flag = False
           break
    if flag:
        new_tpl = tuple(sorted(lst))
    else:
        new_tpl = tuple(lst)
    return new_tpl


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
