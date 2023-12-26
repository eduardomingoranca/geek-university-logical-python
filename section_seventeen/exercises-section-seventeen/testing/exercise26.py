"""
Escreva um codigo que apresente a classe Microondas, com atributo
ligado e o metodo imprimir. O metodo imprimir deve mostrar na tela os valores
de todos os atributos. O atributo ligado sera boolean e devera indicar o estado
atual do microondas, se ligado ou desligado.
"""
from classes.house import Microwave

m1 = Microwave(True, False)

print(m1.__print__())

m2 = Microwave(False, True)

print(m2.__print__())
