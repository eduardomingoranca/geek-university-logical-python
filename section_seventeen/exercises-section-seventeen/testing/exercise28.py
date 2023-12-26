"""
Baseando-se no exercicio 27 adicione os metodos ligar e desligar que deverao
mudar o conteudo do atributo ligado conforme o caso.
"""
from classes.house import Microwave

m1 = Microwave(True, False)

print(m1.__print__())

m2 = Microwave(False, True)

print(m2.__print__())

