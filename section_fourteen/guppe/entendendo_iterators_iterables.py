"""
Entendendo Iterators e Iterables


Iterator ->
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() eh chamada;

Iterable ->
    - Um objeto que ira retornar um iterator quando a funcao iter() for chamada.


nome = 'Geek'  # Eh um iterable mas nao eh um iterator.
numeros = [1, 2, 3, 4, 5, 6]  # Eh um iterable mas nao eh um iterator.

it1 = iter(nome)
it2 = iter(numeros)


print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))


print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
"""


nome = 'Geek'

for letra in nome:
    print(f'{letra}')
