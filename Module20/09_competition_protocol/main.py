def input_protocol(index, protocol):
    entry = input('{0}-я запись: '.format(index)).split()
    if entry[1] in protocol:
        if int(entry[0]) > protocol[entry[1]][0]:
            protocol[entry[1]][0] = int(entry[0])
            protocol[entry[1]][1] += 1
    else:
        new_lst = [int(entry[0]), 1]
        protocol[entry[1]] = new_lst
    return protocol

def winer(protocol):
    winer_lst = []
    while len(winer_lst) < 3:
        winer = [0, 0, 0]
        for i_name, i_score in protocol.items():
            if i_score[0] > winer[1]:
                winer[0], winer[1], winer[2] = i_name, i_score[0], i_score[1]
            elif i_score[0] == winer[1]:
                if i_score[1] <= winer[2]:
                    winer[0], winer[1], winer[2] = i_name, i_score[0], i_score[1]

        winer_lst.append(winer)
        protocol.pop(winer[0])
        winer = [0, 0, 0]
  # Заменяем попытку на ранг
    winer_lst[0][2] = 1
    for i_winer in range(len(winer_lst) - 1):
        if winer_lst[i_winer][1] == winer_lst[i_winer + 1][1] and winer_lst[i_winer][2] == winer_lst[i_winer + 1][2]:
            winer_lst[i_winer + 1][2] = winer_lst[i_winer][2]
        else:
            winer_lst[i_winer + 1][2] = winer_lst[i_winer][2] + 1

    for winer in winer_lst:
        print('{index}-е место. {name} ({score})'.format(
            index=winer[2],
            name=winer[0],
            score=winer[1]
        ))


count_entry = int(input('Сколько записей вносится в протоколе? '))
print('Записи (результат и имя):')
protocol = dict()
for i_entry in range(1, count_entry + 1):
    protocol = input_protocol(i_entry, protocol)
print('Итоги соревнований:\n')
winer(protocol)