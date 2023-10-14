"""
Receba a altura do degrau de uma escada e a altura que o usuario deseja alcancar
subindo a escada. Calcule e mostre quantos degraus o usuario devera subir para atingir
seu objetivo.
"""
try:
    altura_degrau = float(input('Informe a altura do degrau de uma escada: '))
    altura_escada = float(input('Informe a altura da escada: '))

    while altura_escada < altura_degrau:
        altura_degrau = float(input('Informe a altura do degrau de uma escada: '))
        altura_escada = float(input('Informe a altura da escada: '))

    quantidade_degrau = altura_escada // altura_degrau

    print(f'A quantidade de degraus para atigir o objetivo eh {quantidade_degrau:.0f}')
except ValueError:
    print('O valor informado esta incorreto!')
