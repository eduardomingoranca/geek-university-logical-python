"""
POO - Heranca Multipla

Heranca Multipla nada mais eh do que a possibilidade de uma classe herdar de multiplas classes,
fazendo com que a classe filha herde todos os atributos e metodos de todas as classes herdadas.

#OBS: A heranca multipla pode ser feita de duas maneiras:
    - Por Multiderivacao Direta;
    - Por Multiderivacao Indireta;

# Exemplo 1 - Multiderivacao Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivacao Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


#OBS: Nao importa se a derivacao eh direta ou indireta. A classe que realizar a heranca herdara
todos os atributos e metodos das super classes.
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Eu sou Tux da terra! / Eu sou Tux do mar! ???? Method Resolution Order - MRO


# Objeto eh instancia de...

print(f'Tux eh instancia de Pinguim? {isinstance(tux, Pinguim)}')  # True
print(f'Tux eh instancia de Aquatico? {isinstance(tux, Aquatico)}')  # True
print(f'Tux eh instancia de Terrestre? {isinstance(tux, Terrestre)}')  # True
print(f'Tux eh instancia de Animal? {isinstance(tux, Animal)}')  # True
print(f'Tux eh instancia de object? {isinstance(tux, object)}')  # True

