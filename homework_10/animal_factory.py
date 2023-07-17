# Доработаем задачи 5-6. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов) и
# параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from animal import Fish, Bird, Mammal, Animal


class AnimalFactory:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_type(animal_type)
        return new_animal(*args, **kwargs)

    def _get_type(self, animal_type: str):
        types = {'fish': Fish, 'bird': Bird, 'mammal': Mammal}
        return types[animal_type.lower()]


if __name__ == '__main__':
    animal = AnimalFactory()
    animal_fish = animal.make_animal('fish', 'Neo', 10)
    animal_bird = animal.make_animal('bird', 'Kar', 1)
    animal_mammal = animal.make_animal('mammal', 'Bob', 15)
    print(animal_fish.special_info())
    print(animal_bird.special_info())
    print(animal_mammal.special_info())
