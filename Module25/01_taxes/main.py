class Property:
    """
    Базовый класс, описывающий собственность

    Args:
        worth (int): стоимость недвижимости

    Attributes:
        tax (float): ставка налога по-умолчанию
    """

    tax = 0.13

    def __init__(self, worth):
        self.worth = worth

    def value_tax(self):
        """
        Возвращает сумму налога
        :return: value
        :rtype: float
        """
        value = round(self.worth * self.tax, 2)
        return value


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property

    Attributes:
        tax (float): ставка налога на квартиру

    """

    tax = 1 / 1000


class Car(Property):
    """
        Класс Машина. Родитель: Property

        Attributes:
            tax (float): ставка налога на машину

        """

    tax = 1 / 200


class CountryHouse(Property):
    """
        Класс Дача. Родитель: Property

        Attributes:
            tax (float): ставка налога на дачу

        """

    tax = 1 / 500


def calc_tax():
    """
    Функция для расчета суммы налога на имущество
    """

    print('---РАСЧЕТ СТОИМОСТИ НАЛОГА НА ИМУЩЕСТВО---')
    money = int(input('\nВведите ваш бюджет для уплаты налога: '))
    total_tax = 0
    while True:
        try:
            my_property = input('\nВведите тип собственности(1- Квартира, 2- Машина, 3- Дача, 4- ЗАВЕРШИТЬ): ')
            if my_property != '1' and my_property != '2' and my_property != '3' and my_property != '4':
                raise ValueError
        except ValueError:
            print('\nОшибка, неверный ввод. Попробуйте еще раз.')
        else:
            if my_property == '4':
                break
            price = int(input('Введите стоимость объекта: '))
            if my_property == '1':
                my_property = Apartment(price)
            elif my_property == '2':
                my_property = Car(price)
            elif my_property == '3':
                my_property = CountryHouse(price)
            total_tax += my_property.value_tax()

    if total_tax <= money:
        print(f'\nБюджета {money} хватит для уплаты налогов.\nОбщий налог составил: {total_tax}')
    else:
        print(f'\nБюджета {money} НЕ хватит для уплаты налогов.\nОбщий налог составил: {total_tax}'
              f'\nНеобходимо добавить {total_tax - money}')


calc_tax()
