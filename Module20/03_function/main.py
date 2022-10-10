def slicer(tpl, key):
    lst = list(tpl)
    for num in lst:
        if key in lst:
            start = lst.index(key)
            if key in lst[start+1:]:
                stop = lst[start+1:].index(key) + start + 2
            else:
                stop = len(lst)
        else:
            return ()
    new_tuple = tuple(lst[start:stop])
    return new_tuple

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 10), 2))
