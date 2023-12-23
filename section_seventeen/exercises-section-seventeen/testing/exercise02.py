"""
Baseando-se no exercicio 1 adicione um metodo construtor que permita a
definicao de todos os atributos no momento da instanciacao do objeto.
"""
from classes.user import Person

p1 = Person('Landon Carter', '123 Carston Avenue, Birmingham, AL 35242',
            '13216540987')

print(p1.print())
