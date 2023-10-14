"""
Faca um programa que leia 2 notas de um aluno, verifique se as notas sao validas e
exiba na tela a media destas notas. Uma nota valida deve ser, obrigatoriamente, um
valor entre 0.0 e 10.0, onde caso a nota nao possua um valor valido, este fato deve
ser informado ao usuario e o programa termina.
"""
try:
    nota_um = float(input('Informe a 1ª nota: '))
    nota_dois = float(input('Informe a 2ª nota: '))

    if 0.0 <= nota_um <= 10.0 and 0.0 <= nota_dois <= 10.0:
        print(f'N1: {nota_um} | N2: {nota_dois} | MEDIA: {(nota_um + nota_dois)/2.0}')
    else:
        print('NOTA INVALIDA!')

except ValueError:
    print('O valor informado esta invalido!')
