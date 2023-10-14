"""
Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas.
A formula de conversao eh: P = C/2.54,sendo C o comprimento em centimetros e P o
comprimento em polegadas.
"""
try:
    c = float(input('Informe um valor de comprimento em centimetros: '))
    p = c / 2.54
    print(f'P = {c} / 2.54')
    print(f'P = {p:.2f}')
except ValueError:
    print('O valor informado esta invalido!')
