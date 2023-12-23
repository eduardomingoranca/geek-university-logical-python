"""
Escreva um codigo que apresente a classe Circulo, com atributos raio,
area e perimetro e, os metodos calcularArea, calcularPerimetro e imprimir. Os
metodos calcularArea e calcularPerimetro devem efetuar seus respectivos
calculos e colocar os valores nos atributos area e perimetro. O metodo imprimir
deve mostrar na tela os valores de todos os atributos. Salienta-se que a area de
um circulo eh obtida pela formula (pi * raio * raio) e o perimetro por (2 * pi *
raio), onde pi = 3.141516
"""
from classes.geometric_shapes import Circle

c1 = Circle(2)

print(c1.print())

