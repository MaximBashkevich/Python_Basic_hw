import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('Первая команда:', team_1)
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('Вторая команда:', team_2)
team_3 =[(team_1[i_member] if team_1[i_member] > team_2[i_member] else team_2[i_member]) for i_member in range(20)]
print('Победители тура:', team_3)