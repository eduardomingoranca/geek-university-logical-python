class Person:

    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_height(self):
        return self._height

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_height(self, height):
        self._height = height

    def print_person(self):
        print(self._name)
        print(self._age)
        print(self._height)
