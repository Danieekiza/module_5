class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
        print('')


h1 = House('Самолет', 22)
h2 = House('ПИК', 15)
h1.go_to(13)
h2.go_to(-10)
h2.go_to(16)
