"""
Escreva um codigo que apresente a classe Moto, com atributos marca,
modelo, cor e marcha e,o metodo imprimir. O metodo imprimir deve mostrar na
tela os valores de todos os atributos. O atributo marcha indica em que a marcha
a Moto se encontra no momento, sendo representando de forma inteira, onde 0 - neutro,
1 - primeira, 2 - segunda, etc.
"""
from classes.vehicle import Motorcycle

m1 = Motorcycle('BMW', 'F 850 GS Adventure', 'Black', 2)

print(m1.print())
