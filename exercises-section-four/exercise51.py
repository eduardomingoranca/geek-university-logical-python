"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua
distancia da origem (0,0).
"""
try:
    x = float(input('X: '))
    y = float(input('Y: '))

    if x > 0 and y > 0:
        print('QUADRANTE I')
    elif x < 0 < y:
        print('QUADRANTE II')
    elif x < 0 and y < 0:
        print('QUADRANTE III')
    else:
        print('QUADRANTE IV')

except ValueError:
    print('O valor informado esta invalido!')
