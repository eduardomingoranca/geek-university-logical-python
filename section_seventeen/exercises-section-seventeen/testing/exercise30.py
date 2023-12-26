"""
Baseando-se no exercicio 29 adicione os metodos fecharPorta e abrirPorta que
devera mudar o conteudo do atributo portaFechada conforme o caso.
"""
from classes.house import Microwave

m1 = Microwave(True, False)

print(m1.__print__())

m2 = Microwave(False, True)

print(m2.__print__())
