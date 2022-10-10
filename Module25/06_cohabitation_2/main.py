import random


class MyException(Exception):
    pass


class House:
    """
    Класс Дом

    money (int): Деньги
    fridge (int): Еда в доме
    cat_food (int): Еда кота
    dirt (int): Уровень грязи в доме
    data (list): Данные [заработано денег, съедено еды, куплено шуб] за жизненный цикл

    """
    money = 100
    fridge = 50
    cat_food = 30
    dirt = 0
    residents = []
    data = [0, 0, 0]

    def settle(self, man):
        """
        Добавляет жителя в дом
        :param man: житель
        """
        self.residents.append(man)

    def add_dirt(self, dirt):
        """
        Добавляет грязь в дом
        :param dirt: Грязь
        """
        self.dirt += dirt

    def __str__(self):
        return 'Заработано денег\t{}\nСъедено еды\t{}\nКуплено шуб\t{}'.format(
            self.data[0],
            self.data[1],
            self.data[2]
        )


class Cat:
    """
    Класс Кот
    hunger (int): сытость
    Attributes:
        name (str): Имя
        house (House): Дом
    """
    hunger = 30

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return 'Имя кота\t{}\nСытость\t{}'.format(self.name, self.hunger)

    def eat(self, food):
        """
        Кот ест
        :param food: (int) Еда
        :raise: Ограничение приема пищи
        """
        if self.house.cat_food > 0:
            if food <= 10:
                self.hunger += food
                self.house.cat_food -= food
                self.house.data[1] += food
            else:
                raise MyException('Слишком много еды для кота!')

    def tear_wallpaper(self):
        """
        Кот рвет обои
        """
        self.house.dirt += 5
        self.hunger -= 10

    def sleep(self):
        pass

    def check_life(self):
        """
        Проверка сытости
        """
        if self.hunger <= 0:
            return True


class People:
    """
    Базовый класс Человек
    hunger (int): Сытость
    happy (int): Уровень счастья

    Attributes:
        name (str): Имя
        house (House): Дом
    """
    hunger = 30
    happy = 100

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return 'Имя\t{}\nСытость\t{}\nСчастье\t{}'.format(self.name, self.hunger, self.happy) + '\n'

    def pet_cat(self):
        """
        Гладим кота
        """
        self.happy += 5

    def eat(self, food):
        """
        Человек ест
        :param food: (int) Еда
        :raise: Ограничение приема пищи
        """
        if self.house.fridge > 0:
            if food <= 30:
                self.hunger += food
                self.house.fridge -= food
                self.house.data[1] += food
            else:
                raise MyException('Слишком много еды для человека!')

    def check_life(self):
        """
        Проверка сытости и уровня счастья
        """
        if self.hunger <= 0 or self.happy <= 0:
            return True


class Men(People):
    """
    Класс Мужчина. Родитель People
    """
    def work(self):
        """
        Мужчина работает
        """
        self.house.money += 150
        self.hunger -= 10
        self.house.data[0] += 150

    def play(self):
        """
        Мужчина играет
        """
        self.happy += 20
        self.hunger -= 10


class Woman(People):
    """
    Класс Женщина. Родитель People
    """
    def shopping(self, products):
        """
        Покупка продуктов/корма для кота/шубы
        :param products: (int) Количество продуктов
        """
        if self.house.money > 10:
            self.house.money -= products
            self.house.fridge += products
        elif self.house.money > 10:
            self.house.money -= products
            self.house.cat_food += products
        if self.house.money > 350:
            self.house.money -= 350
            self.happy += 60
            self.house.data[2] += 1

    def cleaning(self, count):
        """
        Уборка в доме
        :param count: (int) количество грязи
        """
        self.house.dirt -= count


def day_from_life(resident, number):
    """
    Прожитый день человека/кота
    :param resident: (People/Cat) житель дома
    :param number: (int) случайное число
    :return: (Bool)
    """
    if isinstance(resident, Men):
        if resident.house.money < 100 or number % 10 == 0:
            resident.work()
        elif resident.happy < 50:
            resident.play()
        elif resident.happy < 80:
            resident.pet_cat()
        else:
            resident.eat(number)
    elif isinstance(resident, Woman):
        if resident.house.fridge < 50:
            resident.shopping(number)
        elif resident.house.dirt > 50:
            resident.cleaning(number)
        elif resident.happy < 80:
            resident.pet_cat()
        else:
            resident.eat(number)
    elif isinstance(resident, Cat):
        if resident.hunger < 20:
            resident.eat(number)
        elif resident.hunger < 30:
            resident.tear_wallpaper()
            resident.eat(number)
        else:
            resident.sleep()
    if resident.check_life():
        return True
    else:
        return False


def cohabitation():
    """
    Жизненный цикл сожителей
    """
    men_name = input('Введите именя мужчины: ')
    woman_name = input('Введите именя женщины: ')
    cat_name = input('Как зовут кота: ')
    house = House()
    men = Men(men_name, house)
    house.settle(men)
    woman = Woman(woman_name, house)
    house.settle(woman)
    cat = Cat(cat_name, house)
    house.settle(cat)

    for day in range(1, 366):
        for resident in house.residents:
            random_number = random.randint(5, 15)
            if day_from_life(resident, random_number):
                print('{} умер на {}-й день'.format(resident.name, day))
                break
    print('\nЗА ГОД:\n')
    print(house)


cohabitation()
