import math


class Circle:

    abscissa = 0
    ordinate = 0
    radius = 1

    def __init__(self, abscissa, ordinate, radius):
      self.abscissa = abscissa
      self.ordinate = ordinate
      self.radius = radius

    def calculation_perimeter(self):
        perimeter = round(2 * math.pi * self.radius, 2)
        print('Периметр круга равен:', perimeter)

    def calculation_square(self):
        square = round(math.pi * self.radius ** 2, 2)
        print('Площадь круга равна:', square)

    def increase(self):
        coef = input('Во сколько раз увеличиваем круг: ')
        if '.' in coef:
            self.radius *= float(coef)
        else:
            self.radius *= int(coef)
        print('Радиус круга теперь:', self.radius)

    def intersection(self):
        user_data = input('Введите координаты X, Y и радиус второго круга(через пробел): ').split()
        line = math.sqrt((self.abscissa - int(user_data[0])) ** 2 + (self.ordinate - int(user_data[1])) ** 2)
        if line <= (self.radius + int(user_data[2])):
            print('\nОкружности пересекаются.')
        else:
            print('\nОкружности не пересекаются.')


def circle_action():
    print('ВВЕДИТЕ ДАННЫЕ КРУГА')
    x_coordinate = int(input('\nВведите координату центра Х: '))
    y_coordinate = int(input('Введите координату центра Y: '))
    radius = int(input('Введите радиус: '))
    circle = Circle(x_coordinate, y_coordinate, radius)
    while True:
        action = input('\n***Выберите действие***\n'
                       '1. Площадь'
                       '\n2. Периметр'
                       '\n3. Увеличение радиуса'
                       '\n4. Пересечение с другим кругом\n')
        if action == '1':
            circle.calculation_square()
        elif action == '2':
            circle.calculation_perimeter()
        elif action == '3':
            circle.increase()
        elif action == '4':
            circle.intersection()
        else:
            print('Выход')
            break


circle_action()
