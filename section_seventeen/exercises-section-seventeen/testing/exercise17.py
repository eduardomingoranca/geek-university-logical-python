"""
Escreva um codigo que apresente a classe Eletrodomestico, com
atributo ligado e o metodo imprimir. O metodo imprimir deve mostrar na tela os
valores de todos os atributos. O atributo ligado sera booleano e devera indicar o
estado atual do eletrodomestico, se ligado ou desligado.
"""
from classes.house import HouseholdAppliance

h1 = HouseholdAppliance(False)

print(h1.__print_household_appliance__())
