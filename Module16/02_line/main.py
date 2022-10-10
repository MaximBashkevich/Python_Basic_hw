def sort_student(line):
    temp = 0
    for i_student in range(len(line)):
        for num in range(len(line)):
            if line[num] > line[i_student]:
                temp = line[i_student]
                line[i_student] = line[num]
                line[num] = temp

    return(line)


line_1 = list(range(160, 177, 2))
line_2 = list(range(162, 181, 3))

line_1.extend(line_2)
sort_line = sort_student(line_1)

print('Отсортированный список учеников', sort_line)