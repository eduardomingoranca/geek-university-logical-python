"""
Faca um programa para ler as dimensoes de um terreno (comprimento c e largura l),
bem como o preco do metro de tela p. Imprima o custo para cercar este mesmo terreno
com tela.
"""
try:
    c = float(input('Informe o comprimento do terreno: '))
    l = float(input('Informe a largura do terreno: '))
    p = float(input('Informe o preco do metro de tela - R$ '))

    print(f'O custo para cercar o terreno com tela de {c}m comprimento e {l}m largura e '
          f'de R$ {(c * l) * p}')
except ValueError:
    print('O valor informado esta invalido!')
