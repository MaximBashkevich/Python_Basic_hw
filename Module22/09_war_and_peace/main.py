import zipfile
import os

def frequence_analysis(file_name):
    sym_dict = {}
    path = os.path.join(file_name)
    current_file = open(path, 'r', encoding='utf-8')
    new_file = open('analysis.txt', 'w', encoding='utf-8')
    for i_line in current_file:
        for i_sym in i_line:
            if i_sym.isalpha():
                if i_sym.lower() in sym_dict:
                    sym_dict[i_sym.lower()] += 1
                else:
                    sym_dict[i_sym.lower()] = 1

    sorted_sym_dict = {}
    sorted_keys = sorted(sym_dict,
                         key=sym_dict.get,
                         reverse=True)
    for key in sorted_keys:
        sorted_sym_dict[key] = sym_dict[key]

    new_file.write('Количество символов в тексте:\n')
    for key, value in sorted_sym_dict.items():
        new_file.write(key.upper() + '- ' + str(value) +'\n')




file_name = 'voyna-i-mir.txt'
archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
archive.extract(file_name)
archive.close()
frequence_analysis(file_name)
