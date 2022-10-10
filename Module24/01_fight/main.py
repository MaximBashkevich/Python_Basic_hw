import random

class Warriors:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20


    def death_warrior(self):
        if self.health <= 0:
            return False
        else:
            return True


    def damage_to_warrior(self):
        self.health -= 20


def battle():
    members = []
    player_name_1 = input('Введите имя первого воина: ')
    player_1 = Warriors(player_name_1)
    player_name_2 = input('Введите имя второго воина: ')
    player_2 = Warriors(player_name_2)
    members.append(player_1)
    members.append(player_2)
    print('\n--------------------------Игра началась--------------------------')
    lap = 1
    while True:
        temp = input('\nНажмите Enter')
        #if all([player.death_warrior for player in members]):
        if player_1.death_warrior() and player_2.death_warrior():
            index = random.randint(0, 1)
            attacking_player = members[index]
            accepting_player = members[1 - members.index(attacking_player)]
            accepting_player.damage_to_warrior()


            if player_1.death_warrior() and player_2.death_warrior():
                print('\n{}-й раунд.\n{} нанес удар.\nУ {} осталось здоровья: {}'.format(
                lap, attacking_player.name, accepting_player.name, accepting_player.health
            ))
            else:
                print('\n--------------------------Игра окончена--------------------------\n{} победил!!!'.format(
                    attacking_player.name))
                break
    lap += 1


battle()
