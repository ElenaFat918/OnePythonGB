# Урок 10. ООП. Начало
# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animals:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_animal(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age} лет")


class Fish(Animals):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def swim(self):
        print(f"{self.name} плывет по воде.")

    def info_animal(self):
        super().info_animal()
        print(f"Цвет: {self.color}")


class Birds(Animals):

    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} летит по воздуху.")

    def info_animal(self):
        super().info_animal()
        print(f"Размах крыльев: {self.wingspan} см")


class Mammals(Animals):

    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def walk(self):
        print(f"{self.name} идет по земле.")

    def info_animal(self):
        super().info_animal()
        print(f"Вид: {self.species}")

fish = Fish("Немо", 2, "оранжевый")
fish.swim()
fish.info_animal()

print()        

birds = Birds("Кеша", 1, 10)
birds.fly()
birds.info_animal()

print()

mammals = Mammals("Корова", 3, "ферма")
mammals.walk()
mammals.info_animal()