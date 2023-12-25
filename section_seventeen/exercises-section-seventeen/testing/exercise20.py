"""
Escreva um codigo que apresente a classe Televisor, com atributos
ligado, canal e volume e, o metodo imprimir. O metodo imprimir deve mostrar
na tela os valores de todos os atributos. O atributo ligado sera booleano e devera
indicar o estado atual do televisor, se ligado ou desligado. O atributo canal
devera indicar o canal atual em que o televisor esta sintonizado. O atributo
volume devera indicar o volume atual do televisor.
"""
from classes.house import Television

t1 = Television(True, 4, 25, 'null', 'null')

print(t1.print())
