"""
Faca um programa que calcule o menor numero divisivel por cada um dos numeros de 1
a 20? Exemplo: 2520 eh o menor que pode ser dividido por cada um dos numeros de 1
a 10, sem sobrar resto.
"""
from math import lcm

print(lcm(*range(2, 21)))


