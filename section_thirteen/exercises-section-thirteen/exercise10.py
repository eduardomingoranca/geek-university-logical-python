"""
Faca um programa que receba o nome de um arquivo de entrada e outro de saida. O
arquivo de entrada contem em cada linha o nome de uma cidade (ocupando 40 caracteres)
e o seu numero de habitantes. O programa devera ler o arquivo de entrada e gerar
um arquivo de saida onde aparece o nome da cidade mais populosa seguida pelo seu
numero de habitantes.
"""

cities = open('files/cities.txt').read()

with open('files/most_populated_city.txt', 'w') as file:
    file.write(cities[slice(0, 15)])

print(open('files/most_populated_city.txt').read())
