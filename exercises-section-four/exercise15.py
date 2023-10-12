"""
Leia um angulo em radianos e apresente-o convertido em graus. A formula de conversao
eh: G = R * 180 / pi, sendo G o angulo em graus e R em radianos e pi = 3.14
"""
import math

try:
    r = float(input('Informe um angulo em radianos: '))
    g = r * 180 / math.pi
    print(f'G = {r} * 180 / {math.pi}')
    print(f'G = {g:.2f}')
except ValueError:
    print('O valor informado esta invalido!')
