"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A formula de conversao eh: C = P * 2.54, sendo C o comprimento em centimentos e P o
comprimento em polegadas
"""
try:
    p = float(input('informe um valor de comprimento em polegadas: '))
    c = p * 2.54
    print(f'C = {p} * 2.54')
    print(f'C = {c}')
except ValueError:
    print('O valor informado esta invalido!')