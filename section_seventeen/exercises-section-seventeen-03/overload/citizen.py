class Person:

    def __init__(self, code, name, age):
        self.__code = code
        self.__name = name
        self.__age = age

    def __print__(self, has_age=None):
        if has_age == 1:
            return f'{self.__name} tem {self.__age} anos de codigo {self.__code}'
        return f'{self.__name} tem o codigo {self.__code}'
