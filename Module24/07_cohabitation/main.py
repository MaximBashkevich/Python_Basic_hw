import random

class House:
    fridge = 50
    money = 0
    residents = []

    def settle(self, man):
        self.residents.append(man)


class Man:
    hunger = 50

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def check_life(self):
        if self.hunger > 0:
            return True
        else:
            return False

    def eat(self):
        if self.house.fridge > 0:
            self.hunger += 1
            self.house.fridge -= 1

    def work(self):
        self.house.money += 1
        self.hunger -= 1

    def play(self):
        self.hunger -= 1

    def shopping(self):
        if self.house.money > 10:
            self.house.money -= 10
            self.house.fridge += 10


def day_from_life(man, number):
    if man.hunger < 20:
        man.eat()
        if man.house.fridge < 10:
            man.shopping()
            if man.house.money < 50:
                man.work()
    elif number == 1:
        man.work()
    elif number == 2:
        if man.house.fridge > 0:
            man.eat()
    if man.check_life():
        return True
    else:
        return False


def cohabitation():
    men_name = input('Введите именя мужчины: ')
    woman_name = input('Введите именя женщины: ')
    house = House()
    men = Man(men_name, house)
    house.settle(men)
    woman = Man(woman_name, house)
    house.settle(woman)

    for day in range(365):
        for man in house.residents:
            cube = random.randint(1, 6)
            if not day_from_life(man, cube):
                print('{} умер от голода на {}-й день'.format(man.name, day))
                break
    print('\nИмя- {}'
          '\nСытость- {}'
          '\nИмя- {}'
          '\nСытость- {}'
          '\nЕды в доме- {}'
          '\nДенег в доме- {}'.format(
        men.name,
        men.hunger,
        woman.name,
        woman.hunger,
        man.house.fridge,
        man.house.money
    ))


cohabitation()
