'''
Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного использования таких объектов?

По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон, цвет и др.

Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование
(в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
'''

class Figure:
    '''
    Атрибуты класса Figure: sides_count = 0
    Каждый объект класса Figure должен обладать следующими атрибутами:
    Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
    Атрибуты(публичные): filled(закрашенный, bool)
    И методами:
    Метод get_color, возвращает список RGB цветов.
    Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета.
    Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
    предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
    возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    Метод get_sides должен возвращать значение я атрибута __sides.
    Метод __len__ должен возвращать периметр фигуры.
    Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.
    '''
    SILENT_MODE = True

    def __init__(self, sides_count, rgb_tuple, *sides):
        if not Figure.SILENT_MODE:
            print(f'Figure.__init__: Длина списка сторон на входе {len(sides)}')
            print(f'Figure.__init__: Список сторон на входе = {sides}')
        self.sides_count = sides_count
        #список длин сторон:
        self.__sides = [1 for _ in range(sides_count)]
        self.set_sides(*sides)
        #список каналов цветов:
        self.__color = (0, 0, 0)
        r, g, b = rgb_tuple
        self.set_color(r, g, b)
        #заливка:
        self.filled = True
        if not Figure.SILENT_MODE:
            print(f'Figure.__init__: Финальная длина списка сторон {len(self.__sides)}')
            print(f'Figure.__init__: Финальный список сторон = {self.__sides}')

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for c in [r, g, b]:
            if type(c) != int:
                if not Figure.SILENT_MODE:
                    print('__is_valid_color: ошибка типа одного из каналов цвета')
                return False
            if c < 0 or c > 255:
                if not Figure.SILENT_MODE:
                    print('__is_valid_color: ошибка значения цветового канала')
                return False
        #если всё ок:
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        elif not Figure.SILENT_MODE:
            print(f'Figure: Цвет ({r}, {g}, {b}) не может быть установлен.')

    def __is_valid_sides(self, *sides_int_list):
        if len(sides_int_list) != self.sides_count:
            if not Figure.SILENT_MODE:
                print(f'__is_valid_sides: Длина списка сторон {len(sides_int_list)} и количество сторон {self.sides_count} фигуры не равны.')
                print(f'__is_valid_sides: Список сторон на входе функции = {sides_int_list}')
            return False
        for side in sides_int_list:
            if isinstance(side, int):
                if side < 0:
                    return False
            else:
                return False
        # если всё ок:
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        for side in self.__sides:
            perimetr += side
        return perimetr

    def set_sides(self, *new_sides):
        if not Figure.SILENT_MODE:
            print(f'set_sides: Длина списка сторон на входе {len(new_sides)}')
            print(f'set_sides: Список сторон на входе = {new_sides}')
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __str__(self):
        info = f'\nFigure:\n - sides_count = {self.sides_count}'
        info += f'\n - sides = {self.__sides}\n - color = {self.__color}\n - filled = {self.filled}'
        info += f'\n - P = len() = {len(self)}'
        return info


class Circle(Figure):
    '''
    Атрибуты класса Circle: sides_count = 1
    Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure
    Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
    Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    '''
    PI_CONST = 3.141592653589793

    def __init__(self, rgb_tuple, *sides):
        super().__init__(1, rgb_tuple, *sides)
        self.__radius = self.get_radius()

    def get_radius(self):
        R = len(self) / (2.0 * Circle.PI_CONST)
        # обновляем и возвращаем:
        self.__radius = R
        return R

    def get_square(self):
        return Circle.PI_CONST * self.__radius ** 2

    def __str__(self):
        info = super().__str__()
        info += f'\n   Circle:'
        info += f'\n    - radius = {self.get_radius()}'
        info += f'\n    - area = {self.get_square()}'
        return info

class Triangle(Figure):
    '''
    Атрибуты класса Triangle: sides_count = 3
    Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure
    Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
    Метод get_square возвращает площадь треугольника.
    '''
    def __init__(self, rgb_tuple, *sides):
        super().__init__(3, rgb_tuple, *sides)
        self.__height = self.get_heights()

    def get_square(self):
        '''По формуле через полупериметр:'''
        half_P = 0.5 * len(self)
        p = half_P
        for side in self.get_sides():
            p *= (half_P - side)
        return p ** 0.5

    def get_heights(self):
        '''У треугольника есть три высоты:'''
        area = self.get_square()
        heights = []
        for side in self.get_sides():
            heights.append(2 * area / side)
        #обновляем и возвращаем:
        self.__height = heights
        return heights

    def __str__(self):
        info = super().__str__()
        info += f'\n   Triangle:'
        info += f'\n    - heights = {self.get_heights()}'
        info += f'\n    - area = {self.get_square()}'
        return info

class Cube(Figure):
    '''
    Атрибуты класса Cube: sides_count = 12
    Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure.
    Переопределить __sides сделав список из 12 одинаковыx сторон (передаётся 1 сторона)
    Метод get_volume, возвращает объём куба.
    '''
    SILENT_MODE = True

    def __init__(self, rgb_tuple, *one_side):
        if len(one_side) == 1:
            value = one_side[0]
        else:
            value = 1
        self.__sides = [value for _ in range(12)]
        if not Cube.SILENT_MODE:
            print(f'Cube: len(one_side) = {len(one_side)}, one_side[0] = {one_side[0]}')
            print(f'Cube: self.__sides = {self.__sides}')
        super().__init__(12, rgb_tuple, *self.__sides)

    def get_volume(self):
        return self.__sides[0] ** 3

'''
ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
'''

def geometry_test():
    print('Geometry test:')
    rectangle = Figure(4, (255, 255, 255), 5, 7, 5, 7)
    print(len(rectangle))
    print(rectangle)

    circle = Circle((127, 127, 127), 1000)
    print(circle)

    triangle = Triangle((64, 64, 64), 3, 4, 5)
    print(triangle)

def main():
    print('\nКод для проверки:')
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    #print(Cube.mro())
    #print(cube1.__dir__())

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

if __name__ == '__main__':
    geometry_test()
    main()

'''
Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216'''