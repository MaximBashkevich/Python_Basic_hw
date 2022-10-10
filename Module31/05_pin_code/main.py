import itertools


numbers = '0123456789'
for pin in itertools.permutations(numbers, 4):
    print(pin)

