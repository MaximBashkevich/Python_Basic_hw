class Person:
    """
    Базовый класс, описывающий человека

    Attributes:
        __name (str): имя
        __age (int): возраст
    """
    info = 'Произошло убийство'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'Имя: {name}\tВозраст: {age}'.format(name=self.__name, age=self.__age)


class Employee(Person):
    """
    Класс Работник. Родитель: Person

    Attributes:
        salary (int): зарплата
    """
    const = 0

    def __init__(self, name, age):
        super().__init__(name, age)
        self.set_salary(self.const)

    def __str__(self):
        info_man = super().__str__()
        info_man = '\t'.join(
            (
                info_man,
                'Зарплата: {}'.format(self.salary)
            )
        )
        return info_man

    def set_salary(self, salary):
        """
        Сеттер для расчета зарплаты
        :param salary: зарплата (по умолчанию 0)
        """
        self.salary = salary


class Manager(Employee):
    """
    Класс Менеджер. Родитель: Employee

    const (int): оклад
    """
    const = 13000


class Agent(Employee):
    """
    Класс Агент. Родитель: Employee

    Attributes:
        sales (int): продажи
    """

    def __init__(self, name, age, sales):
        super().__init__(name, age)
        self.set_salary(sales)

    def set_salary(self, sales):
        """
        Сеттер для расчета зарплаты (переопределяет родительский)
        :param sales: (int) продажи
        """
        self.salary = round(5000 + sales * 0.05)


class Worker(Employee):
    """
    Класс Работник. Родитель: Employee

    Attributes:
        hours (int): количество отработанных часов
    """
    def __init__(self, name, age, hours):
        super().__init__(name, age)
        self.set_salary(hours)

    def set_salary(self, hours):
        """
        Сеттер для расчета зарплаты (переопределяет родительский)
        :param hours: (int) количество отработанных часов
        """
        self.salary = 100 * hours


employee_1 = Manager('Maxim', 32)
employee_2 = Agent('Oleg', 42, 14000)
employee_3 = Worker('Tim', 36, 160)
print(employee_1)
print(employee_2)
print(employee_3)
