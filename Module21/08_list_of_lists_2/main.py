def list_of_lists(my_list, new_list=[]):
    for number in my_list:
        if isinstance(number, int):
            new_list.append(number)
        else:
            list_of_lists(number, new_list)
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(list_of_lists(nice_list))
