def sum_numbers(input_file):
    total_sum = 0
    data_file_1 = open(input_file, 'r')
    data_file_2 = open('answer.txt', 'w')
    for i_line in data_file_1:
        for i_sym in i_line:
            if i_sym.isdigit():
                total_sum += int(i_sym)
    data_file_2.write(str(total_sum))
    data_file_1.close()
    data_file_2.close()


file_name = 'numbers.txt'
sum_numbers(file_name)
