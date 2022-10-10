import random


class KillError(Exception):
    """
    Класс-исключение


    Attributes:
        info (str): информация об исключении для внесения в лог
    """

    info = 'Произошло убийство'


class DrunkError(Exception):
    """
    Класс-исключение


    Attributes:
        info (str): информация об исключении для внесения в лог
    """

    info = 'Употребление алкоголя'


class CarCrashError(Exception):
    """
    Класс-исключение


    Attributes:
        info (str): информация об исключении для внесения в лог
    """

    info = 'Произошла авария'


class GluttonyError(Exception):
    """
    Класс-исключение


    Attributes:
        info (str): информация об исключении для внесения в лог
    """

    info = 'Чревоугодие'


class DepressionError(Exception):
    """
    Класс-исключение


    Attributes:
        info (str): информация об исключении для внесения в лог
    """

    info = 'Депрессия'


class Buddhist:
    """
    Класс с кармой будиста

    __karma (int): уровень кармы
    """

    __karma = 0

    def get_karma(self):
        """
        Геттер для получения кармы будиста
        :return: __karma
        :rtype: int
        """
        return self.__karma

    def set_karma(self, added_karma):
        """
        Сеттер кармы, увеличивает ее на принимаемый параметр
        :param added_karma: плюс к карме
        :type added_karma: int
        """
        self.__karma += added_karma


def one_day(men, day):
    """
    Функция эмитации прожитого дня
    :param men: будист
    :type: экземпляр класса Buddhist

    :param day: номер дня
    :type: int

    :raise KillError, DrunkError, CarCrashError, GluttonyError, DepressionError: с вероятностью 1 к 10

    """
    global event
    fortuna = random.randint(1, 10)
    try:
        exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
        if fortuna == 1:
            event = random.choice(exceptions)
            raise event
    except event:
        with open('karma.log', 'a', encoding='utf-8') as logfile:
            logfile.write(f'На {day}-й день {event.info}\n')
    else:
        karma = random.randint(1, 7)
        men.set_karma(karma)


men = Buddhist()
amount_day = 0
while True:
    amount_day += 1
    if men.get_karma() < 500:
        one_day(men, amount_day)
    else:
        print(f'Просветление достигнуто на {amount_day}-й день.')
        break
