class MyException(Exception):
    """
    Класс-исключение для класса MyDict
    """
    pass


class MyDict:
    """
    Класс-аналог dict с его методами

    dict (dict): пустой словарь
    """

    dict = {}

    def __str__(self):
        text = '{'
        if len(self.dict) != 0:
            for key, value in self.dict.items():
                text += (str(key) + ':' + str(value) + ', ')
            text = text[:len(text) - 2]
            text += '}'
        else:
            text = '{}'

        return text

    def add(self, key, value):
        """
        Добавляет новую пару (ключ, значение) в словарь MyDict
        :param key: новый ключ
        :param value: новое значение
        """
        self.dict[key] = value

    def get(self, key):
        """
        Получает значение словаря по ключу, в случае отсутствия возвращает 0
        :param key: ключ словаря
        :return: value, 0
        """
        if key in self.dict:
            value = self.dict[key]
            return value
        else:
            return 0

    def clear(self):
        """
        Очищает словарь
        """
        self.dict.clear()

    def copy(self):
        """
        Возвращает копию словаря
        :return: new_dict
        :rtype: dict
        """
        new_dict = self.dict.copy()
        return new_dict

    def keys(self):
        """
        Возвращает ключи в словаре
        :return: keys
        :rtype: list
        """
        keys = [key for key, value in self.dict.items()]
        return keys

    def values(self):
        """
        Возвращает значения в словаре
        :return: values
        :rtype: list
        """
        values = [value for key, value in self.dict.items()]
        return values

    def items(self):
        """
        Возвращает пары (ключ, значение)
        :return: values
        :rtype: list
        """
        items = [(key, value) for key, value in self.dict.items()]
        return items

    def pop(self, key):
        """
        Удаляет ключ и возвращает значение. Если ключа нет, кидает исключение
        :param key: ключ
        :return: значение ключа key
        :raise: MyException
        """
        if key in self.dict:
            value = self.dict[key]
            temp = self.dict.pop(key)
            return temp
        else:
            raise MyException('Ключа нет в словаре')


# a = MyDict()
# a.add(1, 2)
# a.add(2, 2)
# a.add(3, 2)
# #a.clear()
#
# print(a.keys())
