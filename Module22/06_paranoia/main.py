import os

def cipher_cezar(string, shift):
    data = 'abcdefghijklmnopqrstuvwxyz'
    new_list = []
    for i_sym in string:
        if i_sym.lower() in data:
            if i_sym.isupper():
                flag = True
            else:
                flag = False
            position = data.index(i_sym.lower())
            new_position = (position + shift) % len(data)
            if flag:
                new_list.append(data[new_position].upper())
            else:
                new_list.append(data[new_position])
        else:
            new_list.append(i_sym)
    new_string = ''.join(new_list)
    return new_string


def cipher_text(file_name):
    path = os.path.join(file_name)
    current_file = open(path, 'r')
    cipher_file = open('cipher_text.txt', 'w')
    shift = 1
    for i_line in current_file:
        new_line = cipher_cezar(i_line, shift)
        cipher_file.write(new_line)
        shift +=1
    current_file.close()
    cipher_file.close()


file_name = 'text.txt'
cipher_text(file_name)
