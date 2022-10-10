from typing import List
from functools import reduce


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

new_floats = list(map(lambda number: round(number ** 3, 3), floats))
new_names = list(filter(lambda name: len(name) >= 5, names))
new_numbers = reduce(lambda number, next_number: number + next_number, numbers)
