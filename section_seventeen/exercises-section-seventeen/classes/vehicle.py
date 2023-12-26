def __motor_gear__(gear):
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


def __lower_gear__(gear):
    if gear < 0:
        return True


def __highest_gear__(gear):
    if gear > 5:
        return True


def __turn_off__(to_connect):
    if not to_connect:
        return 'desligada'


def __turn_in__(to_connect):
    if to_connect:
        return 'ligada'


class Motorcycle:

    def __init__(self, brand, model, color, gear, to_connect):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__gear = gear
        self.__to_connect = to_connect

    def __gear_up__(self, gear):

        if __lower_gear__(gear):
            return invalid_gear

        if __highest_gear__(gear):
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

    def __gear_down__(self, gear):
        if __lower_gear__(gear):
            return invalid_gear

        if __highest_gear__(gear):
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

    def __print__(self):
        if self.__to_connect:
            return (f'{self.__brand}, {self.__model}, {self.__color}, {__motor_gear__(self.__gear)} marcha,'
                    f' a moto esta {__turn_in__(self.__to_connect)}!')

        return (f'{self.__brand}, {self.__model}, {self.__color}, {__motor_gear__(self.__gear)} marcha,'
                f' a moto esta {__turn_off__(self.__to_connect)}!')
