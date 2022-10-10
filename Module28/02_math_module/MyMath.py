from abc import ABC, abstractmethod
from typing import Union


class MyMath(ABC):
    """
    Абстрактный класс, для вычисления периметра, площади и объема фигур
    """
    pi = 3.14

    @classmethod
    @abstractmethod
    def circle_len(cls, radius: Union[float, int]) -> Union[float, int]:
        """
        Метод вычисления длины окружности
        """
        length = 2 * cls.pi * radius
        return length

    @classmethod
    @abstractmethod
    def circle_sq(cls, radius: Union[float, int]):
        """
        Метод вычисления площади круга
        """
        square = cls.pi * radius ** 2
        return square

    @classmethod
    @abstractmethod
    def cube_volume(cls, size: Union[float, int]):
        """
        Метод вычисления объема куба
        """
        volume = size ** 3
        return volume

    @classmethod
    @abstractmethod
    def sphere_volume(cls, radius: Union[float, int]) -> Union[float, int]:
        """
        Метод вычисления объема сферы
        """
        volume = 4 / 3 * cls.pi * radius ** 3
        return volume
