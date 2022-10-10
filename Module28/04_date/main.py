from abc import ABC, abstractmethod


class Date(ABC):
    """Абстрактный класс Дата"""
    DAY = None
    MONTH = None
    YEAR = None

    @classmethod
    @abstractmethod
    def from_string(cls, my_date: str) -> str:
        """
        Метод инициализации атрибутов класса, вывод в текстовом формате
        """
        cls.DAY, cls.MONTH, cls.YEAR = map(int, my_date.split('-'))
        return f'День: {cls.DAY}\tМесяц: {cls.MONTH}\tГод: {cls.YEAR}'

    @classmethod
    @abstractmethod
    def is_date_valid(cls, my_date: str) -> bool:
        """
        Метод проверки даты на корректность
        """
        my_date = my_date.split('-')
        if 1 <= int(my_date[0]) <= 31 and 1 <= int(my_date[1]) <= 12 and int(my_date[2]) > 1:
            return True
        else:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-02-2077'))
print(Date.is_date_valid('40-12-2077'))
