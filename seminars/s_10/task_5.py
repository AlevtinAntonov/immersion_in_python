# Задание №5
# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса

# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name):
        self.name = name


class Fish(Animal):
    def __init__(self, name, habitat_depth):
        super().__init__(name)
        self.description = None
        self.habitat_depth = habitat_depth

    def desc_habitat(self):
        if self.habitat_depth > 100:
            self.description = 'Глубоководная'
        elif self.habitat_depth < 5:
            self.description = 'Мелководная'
        else:
            self.description = 'Обычная'
        return self.description

    def special_info(self):
        return f'Для {self.name} , среда обитания {self.description}'

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wing_length = None
        self.wingspan = wingspan

    def wings_length(self):
        self.wing_length = self.wingspan / 2
        return self.wing_length

    def special_info(self):
        return f'Для {self.name} , крыло {self.wing_length}'

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight_name = self._total_weight()
        self.weight = weight

    def _total_weight(self):
        if self.weight < 5:
            self.weight_name = 'Мелкий'
        elif self.weight < 10:
            self.weight_name = 'Средний'
        else:
            self.weight_name = 'Крупный'
        return self.weight_name

    def special_info(self):
        return f'Для {self.name} , вес {self.weight_name}'

a = Mammal('HHH', 4)
print(a.special_info())