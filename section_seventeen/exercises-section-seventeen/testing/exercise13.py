"""
Baseando-se no exercicio 12 adicione um metodo construtor que permita a
definicao de todos os atributos no momento da instanciacao do objeto.
"""
from classes.vehicle import Motorcycle

m1 = Motorcycle('BMW', 'F 850 GS Adventure', 'Yellow', 2, 'null')

print(m1.__gear_up__(3))
print(m1.__gear_down__(2))
