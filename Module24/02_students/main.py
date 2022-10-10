import random


class Student:

    def __init__(self, name, group_number, progress):
        self.name = name
        self.group_number = group_number
        self.progress = progress

    def print_info(self):
        print(self.name, self.group_number, self.progress, end=' ')
        avarege = self.average_rating()
        print('Средний балл:', avarege)

    def average_rating(self):
        average = round(sum(self.progress) / 5, 2)
        return average


def generator_group():
    names = ['Максим ', 'Илья ', 'Олег ', 'Александр ', 'Антон ', 'Валерий ', 'Игнат ']
    surnames = ['Аршавин', 'Карпин', 'Акинфеев', 'Кержаков', 'Дзюба', 'Смолов', 'Дзагоев']

    students_group = [Student((random.choice(names) + random.choice(surnames)),
                              'Группа №' + str(random.randint(1, 20)),
                              [random.randint(1, 5) for _ in range(5)])
                      for _ in range(10)]

    sorted_group = sorted(students_group, key=Student.average_rating, reverse=True)

    print('\nСписок студентов:\n')
    for line in sorted_group:
        line.print_info()


generator_group()
