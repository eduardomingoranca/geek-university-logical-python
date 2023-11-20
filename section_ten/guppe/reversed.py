"""
Reversed

OBS: Nao confunda com a funcao reserve() que estudamos nas listas.

A funcao reverse() so funciona em listas.

Ja a funcao reversed() funciona com qualquer iteravel.

Sua funcao eh inverter o iteravel.

A funcao reversed() retorna um iteravel chamado List Reverse Iterator

"""

# Exemplos

TEXTO = 'Geek University'

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, nao definimos a ordem dos elementos
# Conjunto (Set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed(TEXTO):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed(TEXTO))))

# Ja vimos como fazer isso mais facil com o slice de strings
print(TEXTO[::-1])

# Podemos tambem utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que tambem ja vimos como fazer isso utilizando o proprio range()
for n in range(9, -1, -1):
    print(n)
