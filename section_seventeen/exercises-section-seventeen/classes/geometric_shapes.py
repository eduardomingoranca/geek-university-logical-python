import math


class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * math.pow(self.__radius, 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def print(self):
        return f'Area: {self.calculate_area()}, Perimeter: {self.calculate_perimeter()}'


class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * self.__length + 2 * self.__width

    def print(self):
        return f'Area: {self.calculate_area()}, Perimeter: {self.calculate_perimeter()}'


class Square:

    def __init__(self, side):
        self.__side = side

    def calculate_area(self):
        return math.pow(self.__side, 2)

    def calculate_perimeter(self):
        return self.__side * 4

    def print(self):
        return f'Area: {self.calculate_area()}, Perimeter: {self.calculate_perimeter()}'
