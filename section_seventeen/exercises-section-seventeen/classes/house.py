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

    def __init__(self, connected, channel, volume):
        self.__connected = connected
        self.__channel = channel
        self.__volume = volume

    def print(self):
        if self.__connected:
            return (f'O televisor esta {turn_in(self.__connected)}, no canal {self.__channel} o volume esta no'
                    f' {self.__volume}')
        return f'O televisor esta {turn_off(self.__connected)}'
