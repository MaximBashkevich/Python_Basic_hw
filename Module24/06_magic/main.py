class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Meat):
            return Soup()
        else:
            return None


class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Meat):
            return Grill()
        else:
            return None


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Meat):
            return Jamon()
        else:
            return None


class Earth:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Water):
            return Dirt()
        else:
            return None


class Meat:
    name = 'Мясо'

    def __add__(self, other):
        if isinstance(other, Air):
            return Jamon()
        if isinstance(other, Fire):
            return Grill()
        if isinstance(other, Water):
            return Soup()
        else:
            return None


class Steam:
    name = 'Пар'


class Lightning:
    name = 'Молния'


class Storm:
    name = 'Шторм'


class Dust:
    name = 'Пыль'


class Dirt:
    name = 'Грязь'


class Lava:
    name = 'Лава'


class Jamon:
    name = 'Хамон'


class Grill:
    name = 'Мясо гриль'


class Soup:
    name = 'Суп'


# a = Water()
# b = Earth()
# c = b + a
# print(c.name)
