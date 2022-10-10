
class Parents:
    children = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.children = children

    def soothe_child(self, child):
        if child in self.children:
            child.soothe()

    def feed(self, child):
        if child in self.children:
            child.eat()

    def add_child(self, child):
        if (self.age - child.age) > 16:
            self.children.append(child)
        else:
            print('{} не может быть ребенком {}'.format(child.name, self.name))

    def parent_info(self):
        print('Имя родителя: {}\nВозраст родителя: {}\nСписок детей:'.format(self.name, self.age))
        for child in self.children:
            child.child_info()



class Children:
    states_calm = {3: 'Спокоен', 2: 'Напряжен', 1: 'Раздражен'}
    states_hunger = {True: 'Сыт', False: 'Голоден'}

    def __init__(self, name, age, state_calm, state_hunger):
        self.name = name
        self.age = age
        self.state_calm = state_calm
        self.state_hunger = state_hunger

    def soothe(self):
        if self.state_calm < 3:
            self.state_calm += 1

    def eat(self):
        if not self.state_hunger:
            self.state_hunger = True

    def get_hungry(self):
        if self.state_hunger:
            self.state_hunger = False

    def child_info(self):
        states_calm = {3: 'Спокоен', 2: 'Напряжен', 1: 'Раздражен'}
        states_hunger = {True: 'Сыт', False: 'Годен'}
        print('\nИмя ребенка: {}'
              '\nВозраст ребенка: {}'
              '\nСостояние спокойствия: {}'
              '\nСостояние голода: {}'.format(
            self.name,
            self.age,
            states_calm[self.state_calm],
            states_hunger[self.state_hunger]
        )
        )
# parent_1 = Parents('Максим', 31)
# child_1 = Children('Василиса', 3.3, 2, False)
# child_2 = Children('Мария', 0.1, 1, False)
# parent_1.add_child(child_1)
# parent_1.add_child(child_2)
# parent_1.parent_info()
# parent_1.soothe_child(child_1)
# parent_1.parent_info()
# parent_1.feed(child_1)
# parent_1.parent_info()
# child_1.get_hungry()
# child_1.child_info()
