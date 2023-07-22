# Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.


import json


class Serializator:
    def __init__(self, data, name):
        self.data = data
        self.name = name

    def to_json(self):
        with open(self.name, 'w') as file:
            json.dump(self.data, file)

    def from_json(self):
        with open(self.name, 'r') as file:
            data = json.load(file)
        return data


serializator = Serializator(data={'name': 'Konstantinople', 'age': 1000},
                            name='data.json')  # Создаем экземпляр класса Serializator
serializator.to_json()  # Вызываем метод для сериализации данных в JSON
output_data = serializator.from_json()  # Вызываем метод для десериализации данных из JSON

print(output_data)  # Выводим десериализованные данные
