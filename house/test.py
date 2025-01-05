from house.houses import House
import random


def defolt():
    h1 = House('Самолет', 20)
    h2 = House('ПИК', 18)
    return h1, h2


def Test():
    h1, h2 = defolt()
    print(f'__str__\nh1 - {h1} \nh2 - {h2}')
    print(f'__len__\nh1: {h1.number_of_floors} \nh2: {h2.number_of_floors}')
    print(f'__eq__\nh1 == h2: {h1 == h2}\nh1 == 20: {h1 == 20}')
    print(f'__lt__\nh1 < h2: {h1 < h2}\nh1 < 20: {h1 < 20}')
    print(f'__le__\nh1 <= h2: {h1 <= h2}\nh1 <= 20: {h1 <= 20}')
    print(f'__gt__\nh1 > h2: {h1 > h2}\nh1 > 20: {h1 > 20}')
    print(f'__ge__\nh1 >= h2: {h1 >= h2}\nh1 >= 20: {h1 >= 20}')
    print(f'__ne__\nh1 != h2: {h1 != h2}\nh1 != 20: {h1 != 20}')

    print(f'__add__\nh1 = h1 + h2: {h1 + h2}\nh2 = h2 + 10: {h2 + 10}')
    h1, h2 = defolt()
    h1 = 20 + h1
    print(f'__radd__\nh1 = 20 + h1: {20 + h1}')
    h1, h2 = defolt()
    h1 += 100
    print(f'__iadd__\nh1 += 100: {h1}')
    h1, h2 = defolt()
    print(f'__sub__\nh1 = h1 - h2: {h1 - h2}')
    h1, h2 = defolt()
    print(f'__sub__\nh1 = h1 - 10: {h1 - 10}')
    h1, h2 = defolt()
    h1 = 100 - h1
    print(f'__rsub__\nh1 = 100 - h1: {h1}')
    h1, h2 = defolt()
    h1 -= 10
    print(f'__iadd__\nh1 -= 10: {h1}')
    h1, h2 = defolt()
    h1.go_to(8)
    h1.go_to(30)


def Test_history():
    house_name = ['Самолет', 'ПИК', 'СУ1', 'Левл', 'ЛСР', 'ЦДС', 'Марс']
    num = 1
    for name in house_name:
        locals()[f"h{num}"] = House(name, random.randrange(2, 40, 2)) #  создаем в locals переменную 'h'+'num'
        # класс House, name из списка, этаж рандом со 2 по 40 шаг 2
        num += 1

    print(locals()['h1'])  # обращение к переменной, созданной не на прямую
    del (locals()['h1'])
    print(locals()['h2'])
    del (locals()['h2'])
    print('House.houses_history', House.houses_history)


if __name__ == '__main__':
    # Test()
    Test_history()
