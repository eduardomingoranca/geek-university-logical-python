"""
Baseando-se no exercicio 26 adicione um metodo construtor que permita a
definicao de todos os atributos no momento da instanciacao do objeto.
"""
from classes.house import Microwave

m1 = Microwave(False, True)

print(m1.__print__())

m2 = Microwave(True, False)

print(m2.__print__())
