"""
Faca um programa que calcula a associacao em paralelo de dois resistores R1 e R2
fornecidos pelo usuario via teclado. O programa fica pedindo estes valores e calculando
ate que o usuario entre com um valor para resistencia igual a zero.
                        R = R1 * R2
                            R1 + R2
"""
try:
    loop = True
    while loop:
        print('Informe o valor ZERO para parar!')
        r1 = float(input('R1: '))
        r2 = float(input('R2: '))

        if r1 == 0 or r2 == 0:
            loop = False
        else:
            r = (r1 * r2) / (r1 + r2)
            print(f'R = {r:.2f}')

except ValueError:
    print('O formato de valor informado esta invalido!')
