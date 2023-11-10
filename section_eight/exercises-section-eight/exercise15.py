"""
Crie um programa que receba tres valores (obrigatoriamente maiores que zero), representados
as medidas dos tres lados de um triangulo. Elabore funcoes para:
    (a) Determinar se eles lados formam um triangulo, sabendo que:
        <> O comprimento de cada lado de um triangulo eh menor do que a soma dos outros
           dois lados.
    (b) Determinar e mostrar o tipo de triangulo, caso as medidas formem um triangulo.
        Sendo que:
            <> Chama-se equilatero o triangulo que tem tres lados iguais.
            <> Denominam-se isosceles o triangulo que tem o comprimento de dois lados
               iguais.
            <> Rebece o nome de escaleno o triangulo que tem os tres lados diferentes.
"""


def eh_triangulo(l1, l2, l3):
    if (l2 + l3) > l1:
        return True
    elif (l1 + l3) > l2:
        return True
    elif (l1 + l2) > l3:
        return True
    else:
        return False


def tipo_triangulo(l1, l2, l3):
    if l1 == l2 and l2 == l3:
        return 'equilatero'
    elif l1 == l2 or l1 == l3 or l2 == l3:
        return 'isosceles'
    elif l1 != l2 and l2 != l3 and l1 != l3:
        return 'escaleno'


try:
    loop = True
    while loop:
        a = float(input('A: '))
        b = float(input('B: '))
        c = float(input('C: '))

        if a > 0 and b > 0 and c > 0:
            loop = False
            t = eh_triangulo(a, b, c)
            if t:
                print(tipo_triangulo(a, b, c))
            else:
                loop = True
                print('NAO EH UM TRIANGULO!')

except ValueError:
    print('FORMATO INVALIDO!')
