#нейминг переменных указан в условии задачи
def hanoi_towers(n, x, y):
    if n == 0:
        return
    buffer = 6 - x - y
    hanoi_towers(n - 1, x, buffer)
    print('Передвигаем диск', n, 'со стержня', x, 'на стержень', buffer)
    hanoi_towers(n - 1, buffer, x)


hanoi_towers(3, 1, 3)
