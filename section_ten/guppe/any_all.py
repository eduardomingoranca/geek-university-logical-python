"""
Any e All


all() -> Retorna True se todos os elementos do iteravel sao verdadeiros ou ainda se o iteravel esta vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os numeros sao verdadeiro? False

print(all([1, 2, 3, 4]))  # Todos os numeros sao verdadeiro? True

print(all([]))  # Todos os numeros sao verdadeiro? True

print(all((1, 2, 3, 4)))  # Todos os numeros sao verdadeiro? True

print(all({1, 2, 3, 4}))  # Todos os numeros sao verdadeiro? True

print(all('Geek'))  # Todos os numeros sao verdadeiro? True


nomes = ['Charles', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# OBS: Um iteravel vazio convertido em boolean eh False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

any() -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False

nomes = ['Charles', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))


print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))

