"""
Baseando-se no exercicio 24 adicione os metodos volumeAcima e
volumeAbaixo, sendo que o metodo volumeAcima deve modificar o volume
para o proximo nivel de volume possivel, onde ao chegar ao volumeMaximo nao
podera possibilitar que o volume seja alterado. O metodo volumeAbaixo deve
modificar o volume para o nivel imediatamente inferior de volume em relacao
ao volume atual, nao podendo ser menor do que 0, simulando desta forma o
funcionamento de um televisor.
"""
from classes.house import Television

t1 = Television(True, 4, 10, 50, 55)

t1.volume_up()
print(t1.print())

t2 = Television(True, 5, 9, 50, 55)

t2.volume_down()
print(t2.print())
