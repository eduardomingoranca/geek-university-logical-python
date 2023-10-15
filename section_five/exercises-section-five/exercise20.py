"""
Dados tres valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo
e, se forem, se eh um triangulo escaleno, equilatero ou isosceles, considerando os seguintes
conceitos:
        <>  O comprimento de cada lado de um triangulo eh menor do que a soma dos outros
        dois lados.
        <>  Chama-se equilatero o triangulo que tem tres lados iguais.
        <>  Denominam-se isosceles o triangulo que tem o comprimento de dois lados iguais.
        <>  Recebe o nome de escaleno o triangulo que tem os tres lados diferentes.
"""
try:
    a = float(input('A: '))
    b = float(input('B: '))
    c = float(input('C: '))

    if a < (b + c) or b < (a + c) or c < (a + b):
        if a == b and b == c and a == c:
            print('TRIANGULO EQUILATERO!')
        elif a == b or a == c or c == b:
            print('TRIANGULO ISOSCELES!')
        elif a != b and b != c and a != c:
            print('TRIANGULO ESCALENO!')
    else:
        print('NAO EH UM TRIANGULO!')

except ValueError:
    print('O valor informado esta invalido!')
