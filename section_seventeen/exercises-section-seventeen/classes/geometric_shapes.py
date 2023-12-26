import math


class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def __calculate_area__(self):
        return math.pi * math.pow(self.__radius, 2)

    def __calculate_perimeter__(self):
        return 2 * math.pi * self.__radius

    def __print__(self):
        return f'Area: {self.__calculate_area__()}, Perimeter: {self.__calculate_perimeter__()}'


class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def __calculate_area__(self):
        return self.__length * self.__width

    def __calculate_perimeter__(self):
        return 2 * self.__length + 2 * self.__width

    def __print__(self):
        return f'Area: {self.__calculate_area__()}, Perimeter: {self.__calculate_perimeter__()}'


class Square:

    def __init__(self, side):
        self.__side = side

    def __calculate_area__(self):
        return math.pow(self.__side, 2)

    def __calculate_perimeter__(self):
        return self.__side * 4

    def __print__(self):
        return f'Area: {self.__calculate_area__()}, Perimeter: {self.__calculate_perimeter__()}'
