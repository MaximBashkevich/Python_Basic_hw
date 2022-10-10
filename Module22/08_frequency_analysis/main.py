import os

def frequence_analysis(file_name):
    data_sym = 'abcdefghijklmnopqrstuvwxyz'
    sym_dict = {}
    path = os.path.join(file_name)
    current_file = open(path, 'r')
    new_file = open('analysis.txt', 'w')
    for i_line in current_file:
        for i_sym in i_line:
            if i_sym.lower() in data_sym:
                if i_sym.lower() in sym_dict:
                    sym_dict[i_sym.lower()] += 1
                else:
                    sym_dict[i_sym.lower()] = 1

    sum_symbol = sum(sym_dict.values())
    sorted_sym_dict = {}
    sorted_keys = sorted(sym_dict,
                         key=sym_dict.get,
                         reverse=True)
    for key in sorted_keys:
        sorted_sym_dict[key] = round(sym_dict[key] / sum_symbol, 3)

    new_dict = {}
    for sym, value in sorted_sym_dict.items():
        if value in new_dict:
            temp = new_dict[value]
            temp.append(sym)
            new_dict[value] = temp
        else:
            new_dict[value] = list(sym)
    print(new_dict)

    for value, symbols in new_dict.items():
        for symbol in sorted(symbols):
            new_file.write(symbol + ' ' + str(value) +'\n')

    current_file.close()
    new_file.close()


file_name = os.path.join('text.txt')
frequence_analysis(file_name)
