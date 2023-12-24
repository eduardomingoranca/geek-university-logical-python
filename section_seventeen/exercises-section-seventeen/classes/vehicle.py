def motor_gear(gear):
    match gear:
        case 0:
            return 'neutro'
        case 1:
            return 'primeira'
        case 2:
            return 'segunda'
        case 3:
            return 'terceira'
        case 4:
            return 'quarta'
        case 5:
            return 'quinta'


def lower_gear(gear):
    if gear < 0:
        return True


def highest_gear(gear):
    if gear > 5:
        return True


class Motorcycle:

    def __init__(self, brand, model, color, gear):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__gear = gear

    def gear_up(self, gear):

        if lower_gear(gear):
            return 'marcha invalida!'

        if highest_gear(gear):
            return 'marcha invalida!'

        match gear:
            case 0:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha neutra mude para a primeira marcha'
            case 1:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha primeira mude para a segunda marcha'
            case 2:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha segunda mude para a terceira marcha'
            case 3:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha terceira mude para a quarta marcha'
            case 4:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha quarta mude para a quinta marcha'
            case 5:
                return f'{self.__brand}, {self.__model}, {self.__color}, quinta marcha mude para a segunda marcha'

    def gear_down(self, gear):
        if lower_gear(gear):
            return 'marcha invalida!'

        if highest_gear(gear):
            return 'marcha invalida!'

        match gear:
            case 5:
                return f'{self.__brand}, {self.__model}, {self.__color}, quinta marcha mude para a segunda marcha'
            case 4:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha quarta mude para a terceira marcha'
            case 3:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha terceira mude para a segunda marcha'
            case 2:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha segunda mude para a primeira marcha'
            case 1:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha primeira mude para a neutro marcha'
            case 0:
                return f'{self.__brand}, {self.__model}, {self.__color}, marcha neutra'

    def print(self):
        return f'{self.__brand}, {self.__model}, {self.__color}, marcha: {motor_gear(self.__gear)}'

