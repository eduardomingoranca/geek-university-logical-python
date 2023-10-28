"""
Modulo Collections: Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

# Em um dicionario, a ordem de insercao dos elementos nao eh garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')


OrderedDict -> Eh um dicionario, que nos garante a ordem de insercao dos elementos.

# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""
from collections import OrderedDict

# Entendendo a diferenca entre Dict e Ordered Dict

# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True -> Ja que a ordem dos elementos nao importa para o dicionario

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> Ja que a ordem dos elementos importa para o OrderedDict
