"""
Baseando-se no exercicio 22 adicione os atributos numeroCanais e,
volumeMaximo, onde numeroCanais indica o numero maximo de canais que o
televisor pode sintonizar e volumeMaximo indica qual o maior nivel de volume
possivel. O metodo imprimir deve ser modificado de forma a mostrar na tela os
valores de todos os atributos.
"""
from classes.house import Television

t1 = Television(True, 5, 20, 50, 100)

print(t1.print())
