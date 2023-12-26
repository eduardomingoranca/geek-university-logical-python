"""
Escreva um codigo que apresente a classe Retangulo, com atributos
comprimentos, largura, area e perimetro e, os metodos calcularArea,
calcularPerimetro e imprimir. Os metodos calcularArea e calcularPerimetro
devem efetuar seus respectivos calculos e colocar os valores nos atributos area e
perimetro. O metodo imprimir deve mostrar na tela os valores de todos os
atributos. Salienta-se que a area de um retangulo eh obtido pela formula
(comprimento * largura) e o perimetro por (2 * comprimento) + (2 * largura)
"""
from classes.geometric_shapes import Rectangle

r1 = Rectangle(21, 43)

print(r1.__print__())
