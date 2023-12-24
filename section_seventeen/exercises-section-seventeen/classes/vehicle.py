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


invalid_gear = 'marcha invalida!'


def lower_gear(gear):
    if gear < 0:
        return True


def highest_gear(gear):
    if gear > 5:
        return True


def turn_off(to_connect):
    if not to_connect:
        return 'desligada'


def turn_in(to_connect):
    if to_connect:
        return 'ligada'


class Motorcycle:

    def __init__(self, brand, model, color, gear, to_connect):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__gear = gear
        self.__to_connect = to_connect

    def gear_up(self, gear):

        if lower_gear(gear):
            return invalid_gear

        if highest_gear(gear):
            return invalid_gear

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
            return invalid_gear

        if highest_gear(gear):
            return invalid_gear

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
        if self.__to_connect:
            return (f'{self.__brand}, {self.__model}, {self.__color}, {motor_gear(self.__gear)} marcha,'
                    f' a moto esta {turn_in(self.__to_connect)}!')

        return (f'{self.__brand}, {self.__model}, {self.__color}, {motor_gear(self.__gear)} marcha,'
                f' a moto esta {turn_off(self.__to_connect)}!')
