from task_06 import Fish, Birds, Mammals


class AnimalFactory:

    def create_animal(animal_type: str, name: object, age: object, *args: object) -> object:
        if animal_type == "Fish":
            return Fish(name, age, *args)
        elif animal_type == "Birds":
            return Birds(name, age, *args)
        elif animal_type == "Mammals":
            return Mammals(name, age, *args)
        else:
            raise ValueError("Нет такого животного")


animal_factory = AnimalFactory()

fish = animal_factory.create_animal("Fish", "Немо", 2, "оранжевый")
fish.swim()
fish.info_animal()

print()

birds = animal_factory.create_animal("Birds", "Кеша", 1, 10)
birds.fly()
birds.info_animal()

print()

mammals = animal_factory.create_animal("Mammals", "Корова", 3, "ферма")
mammals.walk()
mammals.info_animal()

print()
