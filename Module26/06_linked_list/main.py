class LinkedList:
    """
    Класс Односвязный список
    Attributes:
        data (list): содержание
        length (int): длина списка
    """
    def __init__(self):
        self.data = []
        self.length = 0

    def __str__(self):
        info = ', '.join([str(element) for element in self.data])
        info = ''.join(("[", info, "]"))
        return info

    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        self.length -= 1
        return self.data[self.length]

    def append(self, element: int or str or float) -> None:
        """
        Добавление элемента в конец списка
        """
        self.length += 1
        self.data.append(element)

    def get(self, position: int) -> int or str or float:
        """
        Получение элемента по индексу
        """
        if (position + 1) > len(self.data):
            raise IndexError('Ошибка. Выход за пределы списка')
        else:
            return self.data[position]

    def remove(self, index: int) -> None:
        """
        Удаление элемента по индексу
        """
        if (index + 1) > len(self.data):
            raise IndexError('Ошибка. Выход за пределы списка')
        else:
            self.length -= 1
            self.data.pop(index)


my_list = LinkedList()
my_list.append("10")
my_list.append("20")
my_list.append("30")
for element in my_list:
    print(element, end=' ')
print('\nТекущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
