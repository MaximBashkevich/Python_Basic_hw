class Potatoes:
    states = {0: 'Не посажена', 1: 'Росток', 2: 'Стебель', 3: 'Плоды'}

    def __init__(self, index):
        self.index_potato = index
        self.state = 0

    def potato_info(self):
        print('Картошка №{} в стадии: {}'.format(self.index_potato, Potatoes.states[self.state]))

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.potato_info()

    def ripe(self):
        if self.state == 3:
            return True
        return False


class Gardener:
    harvest = 0

    def __init__(self, count_potatoes, count_garden, name):
        self.gardens = [[Potatoes(potato) for potato in range(1, count_potatoes + 1)]
                        for _ in range(1, count_garden + 1)]
        self.gardener_name = name

    def grow_potatoes(self):
        index_garden = 0
        for garden in self.gardens:
            index_garden += 1
            print('\nГрядка №{}:'.format(index_garden))
            for potato in garden:
                potato.grow()

    def all_is_ripe(self):
        if all([potato.ripe() for potato in self.gardens[0]]):
            print('\nКартошка созрела. Собираем урожай!')
            return False
        else:
            print('\nПоливаем картошку, картошка растет!')
            return True

    #         print('Поливаем картошку, картошка растет!')
    #         farm.grow_potatoes()

    def collect_harvest(self, count):
        self.harvest += count


def happy_farm():
    name = input('Введите имя фермера: ')
    print('\nФермер {} готов к работе!'.format(name))
    count_garden = int(input('Сколько грядок садим: '))
    count_potatoes = int(input('Сколько картошек садим на грядке: '))
    farm = Gardener(count_potatoes, count_garden, name)

    # for garden in farm.gardens:
    #     print('Грядка')
    #     for potato in garden:
    #         potato.potato_info()

    # farm.grow_potatoes()
    # farm.grow_potatoes()
    # farm.grow_potatoes()
    # a = [potato.ripe for garden in farm.gardens for potato in garden]
    # for i in a:
    #     print(i)

    while True:
        if farm.all_is_ripe():
            farm.grow_potatoes()
        else:
            harvest = count_garden * count_potatoes
            farm.collect_harvest(harvest)
            print('\nФермер {} собрал {} картошек.'.format(farm.gardener_name, farm.harvest))
            break


happy_farm()
