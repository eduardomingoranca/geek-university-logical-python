"""
Faca um programa que calcule e mostre a area de um trapezio. Sabe-se que:
    A = (basemaior + basemenor) * altura / 2.0
Lembre-se a base maior e a base menor devem ser numeros maiores que zero.
"""
try:
    loop = True
    while loop:
        base_maior = float(input('base maior do trapezio: '))
        base_menor = float(input('base menor do trapezio: '))
        altura = float(input('altura do trapezio: '))

        if base_maior > 0 and base_menor > 0:
            loop = False
            a = (base_maior + base_menor) * altura / 2.0
            print(f'A = ({base_maior} + {base_menor}) * {altura} / 2.0')
            print(f'A = {a}')
        else:
            print('A BASE MAIOR E A BASE MENOR DEVER SER MAIORES QUE ZERO!')

except ValueError:
    print('O valor informado esta invalido!')
