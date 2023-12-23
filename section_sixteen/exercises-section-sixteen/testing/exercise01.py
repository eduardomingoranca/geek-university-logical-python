"""
Crie uma classe para representar uma pessoa, com os atributos privados de nome,
idade e altura. Crie os metodos publicos necessarios para sets e gets e tambem
um metodo para imprimir os dados de uma pessoa.
"""
from classes.Person import Person

p1 = Person('Lon Hammond', 31, 1.75)

Person.print_person(p1)
