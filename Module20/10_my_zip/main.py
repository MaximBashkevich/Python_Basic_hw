def my_zip(data_1, data_2):
  my_list = [(i_sym, j_sym) for index_1, i_sym in enumerate(data_1) for index_2, j_sym in enumerate(data_2) if index_1 == index_2]
  for pair in my_list:
    print(pair)

data_1 = 'abcd'
data_2 = (1, 2, 3, 4, 5)
data_3 = {'a': 'a1', 'b': 'b1', 'aa': 'a2', 'bb': 'b2'}
data_4 = {'aa': 'a2', 'bb': 'b2'}
new_list = zip(data_1, data_2)
print(new_list)
my_zip(data_1, data_2)
