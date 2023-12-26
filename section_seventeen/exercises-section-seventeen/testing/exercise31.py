"""
Baseando-se no exercicio 30 modifique o metodo ligar para que so ligue o
equipamento quando a porta do mesmo estiver fechada, simulando assim o
funcionamento de um microondas.
"""
from classes.house import Microwave

m1 = Microwave(False, True)

print(m1.__print__())

m2 = Microwave(True, False)

print(m2.__print__())

