"""
Map

Com map, fazemos mapeamento de valores para funcao.

import math


def area(r):
    # Calcula a area de um circulo com raio 'r'.
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map

# Map eh uma funcao que recebe dois parametros: O primeiro a funcao, o segundo um iteravel. Retorna um Map Object

areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

#OBS: Após utilizar a funcao map() depois da primeira utilizacao do resultado, ele zera.

# Para fixar - Map

# Temos dados iteraveis:

# dados: a1, a2, ..., an

# Temos uma funcao:

# Funcao: f(x)

# Utilizamos a funcao map(f, dados) onde map ira 'mapear' cada elemento dos dados e aplicar a funcao.

# O Map Object: f(a1), f(a2), f(...), f(an)
"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londes', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
