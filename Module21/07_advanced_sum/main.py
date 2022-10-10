def advanced_sum(*args):
    sum_numbers = 0
    if len(args) == 1:
        for index, value in enumerate(args[0]):
            if isinstance(value, int):
                sum_numbers += value
            else:
                sum_numbers += advanced_sum(tuple(value))
        return sum_numbers
    else:
        for number in args:
            sum_numbers += number
        return sum_numbers


# print(new_sum(1, 2, 3, 4, 5))
# print(new_sum([[1, 2, [3]], [1], 3]))
