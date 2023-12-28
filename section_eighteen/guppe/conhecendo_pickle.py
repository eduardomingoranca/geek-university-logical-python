"""
Conhecendo o Pickle

A funcao do Pickleerealizar o seguinte processo:

Objeto Python -> Binarizacao

Binarizacao -> Objeto Python

Este processoechamado de serializacao/deserializacao

#OBS: O modulo Pickle naoeseguro contra dados maliciosos eh deste forma
naoerecomendado trabalhar com arquivos pickle vindos de outras pessoas
que voce nao conheca ou de fontes desconhecidas.

# Fazendo a escrita em arquivos pickle


felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} esta comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} esta miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo...')


# Fazer a leitura de dados em arquivos pickle


with open('files/pickle/animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gatoe{type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorroe{type(cachorro)}')
