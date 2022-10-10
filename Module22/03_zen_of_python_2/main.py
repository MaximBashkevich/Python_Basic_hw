import os

def analysis_text(input_file):
    sym_dict = dict()
    count_string = 0
    count_words = 0
    count_sym = 0
    data_file = open(input_file, 'r')
    for i_line in data_file:
        count_string +=1
        for i_sym in i_line:
            if i_sym == ' ' or i_sym == '.':
                count_words += 1
            if i_sym.isalpha():
                count_sym += 1
                if i_sym.lower() in sym_dict:
                    sym_dict[i_sym.lower()] += 1
                else:
                    sym_dict[i_sym.lower()] = 1
    rare_sym = min(sym_dict, key=sym_dict.get)
    print('Количество строк в файле: {0}\n'
          'Количество слов в файле: {1}\n'
          'Количество букв в файле: {2}\n'
          'Наиболее редкая буква: {3}'.format(
        count_string,
        count_words,
        count_sym,
        rare_sym
    ))

file_name = os.path.join('..', '02_zen_of_python', 'zen.txt')
analysis_text(file_name)