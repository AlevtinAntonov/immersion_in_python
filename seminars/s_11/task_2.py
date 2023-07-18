# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Arc:
    """Класс Архив, который хранит пару число и строку. ранее созданные экземпляры сохраняются в list-архив"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.lst_arc = []
        else:
            # cls._instance.lst_arc.append(args)
            cls._instance.lst_arc.append((cls._instance.number, cls._instance.arc_string))

        return cls._instance

    def __init__(self, number, arc_string):
        self.number = number
        self.arc_string = arc_string

    def __str__(self):
        return f'{self.number} , {self.arc_string}, {self.lst_arc}'

    def __repr__(self):
        return f'Arc({self.number}, "{self.arc_string}")'


u_1 = Arc(1, 'One')
print(u_1)
u_2 = Arc(2, 'Two')
print(u_2)
u_3 = Arc(3, 'Three')
print(u_3)
print(repr(u_3))
u_4 = Arc(3, "Three")
print(u_4)


print(f'Документация класса: {Arc.__doc__}')
