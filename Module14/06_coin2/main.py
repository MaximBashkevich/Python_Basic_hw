import math

def find_coin(x, y, r):
    center_dist = math.sqrt(x ** 2 + y ** 2)
    if center_dist <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))
print()
find_coin(x, y, r)


