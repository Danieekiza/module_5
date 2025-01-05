class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)  # добавим в иторию название + этажность
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other if isinstance(
            other, int) else self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other if isinstance(
            other, int) else self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other if isinstance(
            other, int) else self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other if isinstance(
            other, int) else self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other if isinstance(
            other, int) else self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other if isinstance(
            other, int) else self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value if isinstance(value, int) else value.number_of_floors
        return self

    def __radd__(self, value):
        self.number_of_floors += value if isinstance(value, int) else value.number_of_floors
        return self

    def __iadd__(self, value):
        self.number_of_floors += value if isinstance(value, int) else value.number_of_floors
        return self

    def __sub__(self, value):
        self.number_of_floors -= value if isinstance(value, int) else value.number_of_floors
        return self

    def __rsub__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value - self.number_of_floors
            return self

    def __isub__(self, value):
        self.number_of_floors -= value if isinstance(value, int) else value.number_of_floors
        return self

    def __len__(self):  # вызывается len()
        return self.number_of_floors

    def __str__(self):  # вызывается print()
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f'{self} снесён, но он останется в истории')

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor,)
        print()
