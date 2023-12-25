def turn_off(to_connect):
    if not to_connect:
        return 'desligado(a)'


def turn_in(to_connect):
    if to_connect:
        return 'ligado(a)'


class HouseholdAppliance:

    def __init__(self, to_connect):
        self.__to_connect = to_connect

    def get_to_connect(self):
        return self.__to_connect

    def print_household_appliance(self):
        if self.__to_connect:
            return f'O eletrodomestico esta {turn_in(self.__to_connect)}!'
        return f'O eletrodomestico esta {turn_off(self.__to_connect)}!'


class Television:

    def __init__(self, connected, channel, volume, channels_number, max_volume):
        self.__connected = connected
        self.__channel = channel
        self.__volume = volume
        self.__channels_number = channels_number
        self.__max_volume = max_volume

    def channel_above(self):
        if self.__channel < self.__channels_number:
            self.__channel = self.__channel + 1
        else:
            self.__channel = 1

    def channel_below(self):
        if self.__channel <= 1:
            self.__channel = self.__channels_number
        else:
            self.__channel = self.__channel - 1

    def volume_up(self):
        if self.__volume < self.__max_volume:
            self.__volume = self.__volume + 1
        else:
            self.__volume = 0

    def volume_down(self):
        if self.__volume <= 0:
            self.__volume = self.__max_volume
        else:
            self.__volume = self.__volume - 1

    def print(self):
        if self.__connected:
            return (f'O televisor esta {turn_in(self.__connected)}, no canal {self.__channel} o volume esta no '
                    f'{self.__volume} que tem o volume maximo de {self.__max_volume} com '
                    f'{self.__channels_number} canais')
        return f'O televisor esta {turn_off(self.__connected)}'
