import math


class Car:
    """
    Базовый класс Автомобиль
    sum_path (int): пройденный путь автомобиля(по-умолчанию равен 0)

    Attributes:
        coordinate (list): координаты
        angle (int/float): угол движения
    """
    sum_path = 0

    def __init__(self, coordinate, angle):
        self.coordinate = coordinate
        self.angle = angle

    def go(self, path):
        """
        Принимает значение пройденного пути, устанавливает новые координаты авто
        :param path: (int/float) Путь
        """
        self.coordinate[0] += path / math.cos(self.angle)
        self.coordinate[1] += path / math.sin(self.angle)
        self.sum_path += path

    def set_angel(self, new_angel):
        """
        Сеттер угла движения авто
        :param new_angel: int/float) Новый угол движения
        """
        self.angle = new_angel

    def __str__(self):
        return 'Пройден путь: {}\nТекущие координаты: {}'.format(self.sum_path, self.coordinate)


class Bus(Car):
    """
    Класс Автобус. Родитель Car
    __money (int): заработанные деньги (по-умолчанию равен 0)
    __people (int): количество пассажиров (по-умолчанию равен 0)
    __rate (int): стоимость билета
    """
    __money = 0
    __people = 0
    __rate = 25

    def come_in(self, people):
        """
        Добавляет пассажиров в салон автобуса, увеличивает заработанные деньги
        :param people: (int) количество пассажиров
        """
        self.__people += people
        self.__money += self.__rate * people

    def go_out(self, people):
        """
        Высаживает пассажиров
        :param people: (int) количество пассажиров
        """
        self.__people -= people

    def __str__(self):
        info_bus = super().__str__()
        info_bus = '\n'.join(
            (
                info_bus,
                'Количество пассажиров в автобусе: {}'.format(self.__people),
                'Заработано денег: {}'.format(self.__money)
            )
        )
        return info_bus


bus = Bus([0, 0], 4)
for _ in range(10):
    bus.come_in(3)
    bus.go(4)
    bus.set_angel(3)
bus.go_out(4)
print(bus)
