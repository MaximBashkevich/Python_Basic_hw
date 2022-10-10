import os

def analysis_dir(path_to_file,
                 count_file=0,
                 count_dir=0,
                 total_size=0):

    for i_elem in os.listdir(path_to_file):
        path = os.path.join(path_to_file, i_elem)
        if os.path.isfile(path):
            count_file += 1
            total_size += os.path.getsize(path)
        if os.path.isdir(path):
            count_dir += 1
            count_file, count_dir, total_size = analysis_dir(
                path, count_file, count_dir, total_size)
    return count_file, count_dir, total_size

input_path = os.path.abspath(os.path.join('..', '..', 'Module21'))
files, folders, size = analysis_dir(input_path)
size /= 1024
print('{0}\nРазмер каталога (в Кб): {1}\n'
      'Количество подкаталогов: {2}\n'
      'Количество файлов: {3}'.format(
    input_path,
    size,
    folders,
    files
))

