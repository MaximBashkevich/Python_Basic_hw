def invert_text(input_file):
    new_text = ''
    data_file = open(input_file, 'r')
    for i_line in data_file:
        temp = new_text[:]
        new_text = i_line + temp
    data_file.close()
    print(new_text)


file_name = 'zen.txt'
invert_text(file_name)
