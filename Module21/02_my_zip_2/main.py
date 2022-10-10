def min_lenght(*args):
  return range(len(sorted(args, key=len)[0]))


def return_tuple(args, index):
  association = [value_2 for index_1, value_1 in enumerate(args)
            for index_2, value_2 in enumerate(value_1) if index_2 == index]
  return tuple(association)


def test(*args):
  numbers = [return_tuple(args, index) for index in min_lenght(args)]
  print(numbers)


data_1 = {1: 1, 2: 2, 3: 3, 4: 4}
data_2 = '123'
data_3 = 1, 2, 3
test(data_1, data_2, data_3)
