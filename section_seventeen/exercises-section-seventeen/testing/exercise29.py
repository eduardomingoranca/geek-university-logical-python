"""
Baseando-se no exercicio 28 adicione o atributo portaFechada que devera ser
booleano e devera indicar se a porta do microondas esta ou nao fechada. O
metodo imprimir deve ser modificado de forma a mostrar na tela os valores de
todos os atributos.
"""
from classes.house import Microwave

m1 = Microwave(True, False)

print(m1.__print__())

m2 = Microwave(False, True)

print(m2.__print__())


