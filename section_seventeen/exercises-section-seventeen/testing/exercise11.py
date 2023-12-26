"""
Baseando-se no exercicio 10 adicione os metodos marchaAcima e
marchaAbaixo que deverao efetuar a troca de marchas, onde o metodo
marchaAcima devera subir uma marcha, ou seja, se a moto estiver em primeira
marcha, devera ser trocada para a segunda marcha e assim por diante. O metodo
marchaAbaixo devera realizar o oposto, ou seja, descer a marcha. O metodo
imprimir deve ser modificado de forma a mostrar na tela os valores de todos os
atributos.
"""
from classes.vehicle import Motorcycle

m1 = Motorcycle('Yamaha', 'NMAX Connected 160 ABS', 'Red', 1, 'null')

print(m1.__gear_up__(1))
print(m1.__gear_down__(2))
