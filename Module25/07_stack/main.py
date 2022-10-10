class TaskManager:
    """
    Класс менеджер-стеков
    stack (dict): словарь стеков. Ключ- приоритет, значение- задача
    """
    stack = dict()

    def new_task(self, string, number):
        """
        Добавляет в стек новое задание
        :param string: задание
        :param number: приоритет
        """
        if number in self.stack:
            self.stack[number] = self.stack.get(number) + ', ' + string
        else:
            self.stack[number] = string

    def remove(self, string):
        """
        Удаляет из стека задание
        :param string: задание
        """
        if string in self.stack.values():
            self.stack = {key: val for key, val in self.stack.items() if string != val}
        else:
            raise ValueError('Такого задания нет в стеке')

    def __str__(self):
        sorted_stack = [' '.join((str(priority), self.stack[priority]))
                        for priority in sorted(self.stack.keys())]
        sorted_stack = '\n'.join(sorted_stack)
        return sorted_stack


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
