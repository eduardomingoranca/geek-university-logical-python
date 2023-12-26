"""
Escreva um codigo que apresente a classe Pessoa, com atributos nome,
endereco e telefone e, o metodo imprimir. O metodo imprimir deve mostrar na
tela os valores de todos os atributos.
"""
from classes.user import Person

p1 = Person('Garrett Blake', '1234 wikiHow Place, Palo Alto, California 94301',
            '16059713700')

print(p1.__print__())
