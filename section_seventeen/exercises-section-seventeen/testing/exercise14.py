"""
Baseando-se no exercicio 13 adicione o atributo ligada que tera a funcao de
indicar se a moto esta ligada ou nao. Este atributo devera ser do tipo boleano. O
metodo imprimir deve ser modificado de forma a mostrar na tela os valores de
todos os atributos.
"""
from classes.vehicle import Motorcycle

m1 = Motorcycle('Yamaha', 'Crosser S ABS', 'Grey', 4, False)

print(m1.__print__())
