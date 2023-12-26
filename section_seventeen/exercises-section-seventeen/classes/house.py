def __turn_off__(to_connect):
    if not to_connect:
        return 'desligado(a)'


def __turn_in__(to_connect):
    if to_connect:
        return 'ligado(a)'


class HouseholdAppliance:

    def __init__(self, to_connect):
        self.__to_connect = to_connect

    def __get_to_connect__(self):
        return self.__to_connect

    def __print_household_appliance__(self):
        if self.__to_connect:
            return f'O eletrodomestico esta {__turn_in__(self.__to_connect)}!'
        return f'O eletrodomestico esta {__turn_off__(self.__to_connect)}!'


class Television:

    def __init__(self, connected, channel, volume, channels_number, max_volume):
        self.__connected = connected
        self.__channel = channel
        self.__volume = volume
        self.__channels_number = channels_number
        self.__max_volume = max_volume

    def __channel_above__(self):
        if self.__channel < self.__channels_number:
            self.__channel = self.__channel + 1
        else:
            self.__channel = 1

    def __channel_below__(self):
        if self.__channel <= 1:
            self.__channel = self.__channels_number
        else:
            self.__channel = self.__channel - 1

    def __volume_up__(self):
        if self.__volume < self.__max_volume:
            self.__volume = self.__volume + 1
        else:
            self.__volume = 0

    def __volume_down__(self):
        if self.__volume <= 0:
            self.__volume = self.__max_volume
        else:
            self.__volume = self.__volume - 1

    def __print__(self):
        if self.__connected:
            return (f'O televisor esta {__turn_in__(self.__connected)}, no canal {self.__channel} o volume esta no '
                    f'{self.__volume} que tem o volume maximo de {self.__max_volume} com '
                    f'{self.__channels_number} canais')
        return f'O televisor esta {__turn_off__(self.__connected)}'


class Microwave:

    def __init__(self, connected, closed_door):
        self.__connected = connected
        self.__closed_door = closed_door

    def __close_the_door__(self):
        if not self.__closed_door:
            return 'a porta esta fechada'

    def __open_the_door__(self):
        if self.__closed_door:
            return 'a porta esta aberta'

    def __print__(self):
        if not self.__closed_door:
            if self.__connected:
                return f'O microondas esta {__turn_in__(self.__connected)} e {self.__close_the_door__()}'
        return f'O microondas esta {__turn_off__(self.__connected)} e {self.__open_the_door__()}'
