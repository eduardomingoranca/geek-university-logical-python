class Equipment:
    pass


class Computer(Equipment):

    def __init__(self, mouse, keyboard):
        self.__mouse = mouse
        self.__keyboard = keyboard

    def __get_mouse__(self):
        return self.__mouse

    def __set_mouse__(self, value):
        self.__mouse = value

    def __get_keyboard__(self):
        return self.__keyboard

    def __set_keyboard__(self, value):
        self.__keyboard = value

    def __print__(self):
        return f'O computador com o mouse {self.__mouse} e o teclado {self.__keyboard}'
