import os

def to_the_second_round(file_name):
    path = os.path.join(file_name)
    current_file = open(path, 'r')
    new_file = open('second_tour.txt', 'w')
    players_dict = {}
    for i_line in current_file:
        player = i_line.split()
        if len(player) == 1:
            min_score = int(player[0])
        else:
            if int(player[2]) > min_score:
                players_dict[player[0] + ' ' + player[1]] = int(player[2])
    if len(players_dict) > 0:
        sorted_players_dict = {}
        sorted_keys = sorted(players_dict,
                             key=players_dict.get,
                             reverse=True)
        for key in sorted_keys:
            sorted_players_dict[key] = players_dict[key]
        number = 1
        new_file.write(str(len(sorted_players_dict)) + '\n')
        for name, value in sorted_players_dict.items():
            name_list = name.split()
            new_line = str(number) + ') ' + name_list[1][:1] + '. ' + name_list[0] + ' ' + str(value) + '\n'
            new_file.write(new_line)
            number += 1

    current_file.close()
    new_file.close()


file_name = os.path.join('first_tour.txt')
to_the_second_round(file_name)
