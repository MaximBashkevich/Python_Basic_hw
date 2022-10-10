from typing import Union


# from abc import ABC
#
#
# class Figure(ABC):
#     def __init__(self, side):
#         self.side = side
#
#
class Square:
    """
    Базовый класс Квадрат
    Attributes:
        _side: сторона квадрата
    """
    def __init__(self, side: Union[int, float]) -> None:
        self._side = side

    def perimetr_squ(self) -> Union[int, float]:
        """
        Метод вычисления периметра Квадрата
        """
        result = self.side * 4
        return result

    def area_squ(self) -> Union[int, float]:
        """
        Метод расчета площади квадрата
        """
        result = self.side ** 2
        return result

    @property
    def side(self) -> Union[int, float]:
        """
        Геттер стороны квадрата
        """
        return self._side

    @side.setter
    def side(self, value) -> None:
        """Сеттер стороны квадрата"""
        self._side = value


class Triangle:
    """
    Базовый класс Треугольник
    Attributes:
        _base: основание треугольника
        _height: высота треугольника
    """
    def __init__(self, base: Union[int, float], height: Union[int, float]) -> None:
        self._base = base
        self._height = height

    @property
    def base(self) -> Union[int, float]:
        """
        Геттер основания треугольника
        """
        return self._base

    @base.setter
    def base(self, value: Union[int, float]) -> None:
        """
        Сеттер основания треугольника
        """
        self._base = value

    @property
    def height(self) -> Union[int, float]:
        """Геттер высоты треугольника"""
        return self._height

    @height.setter
    def height(self, value: Union[int, float]) -> None:
        """Сеттер высоты треугольника"""
        self._height = value

    def perimetr_tri(self) -> Union[int, float]:
        """
        Метод расчета периметра треугольника
        """
        result = 2 * (self.base / 2 + self.height)
        return result

    def area_tri(self) -> Union[int, float]:
        """
        Метод расчета площади треугольника
        """
        result = self.base / 2 * self.height
        return result


class Pyramid(Triangle, Square):
    """
    Класс Пирамида. Родитель: Треугольник
    Attributes:
        base: основание Пирамиды
        height: высота Пирамиды
    """
    def __init__(self, base: Union[int, float], height: Union[int, float]) -> None:
        super().__init__(base, height)

    def area(self):
        """
        Метод для вычисления площади поверхности Пирамиды
        """
        result = sum([Triangle(self.base, self.height).area_tri() for _ in range(4)]) + Square(self.base).area_squ()
        return result


class Cube(Square):
    """
        Класс Куб. Родитель: Квадрат
        Attributes:
            side: сторона Куба
        """
    def __init__(self, side: Union[int, float]) -> None:
        super().__init__(side)

    def area(self) -> Union[int, float]:
        """
        Метод для вычисления площади поверхности Куба
        """
        result = sum([Square(self.side).area_squ() for _ in range(6)])
        return result


my_figure = Square(4)
print(my_figure.perimetr_squ())
my_figure.side = 12
print(my_figure.perimetr_squ())

my_figure = Triangle(5, 3)
print(my_figure.perimetr_tri())

my_figure = Cube(5)
print(my_figure.area())

my_figure = Pyramid(5, 5)
print(my_figure.area())

my_figure.base = 6
print(my_figure.area())
