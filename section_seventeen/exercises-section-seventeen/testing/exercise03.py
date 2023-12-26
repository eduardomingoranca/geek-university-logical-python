"""
Escreva um codigo que apresente a classe Quadrado, com atributos
lado, area e perimetro e, os metodos calcularArea, calcularPerimetro e imprimir.
Os metodos calcularArea e calcularPerimetro devem efetuar seus respectivos
calculos e colocar os valores nos atributos area e perimetro. O metodo imprimir
deve mostrar na tela os valores de todos os atributos. Salienta-se que a area de
um quadrado eh obtida pela formula (lado * lado) e o perimetro por (4 * lado).
"""
from classes.geometric_shapes import Square

s1 = Square(17)

print(s1.__print__())
