class Person:

    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def print(self):
        return f'{self.__name}, {self.__address}, {self.__phone_number}'
