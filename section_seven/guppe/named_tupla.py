"""
Modulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> Sao tupla, diferenciadas, onde, especificamos um nome para a mesma e tambem parametros.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parametros.

# Forma 1 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 = Declaracao Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)


# Acessando os dados

# Forma 1

print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome


# Forma 2

print(ray.idade)  # idade
print(ray.raca)  # caca
print(ray.nome)  # nome


print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))
