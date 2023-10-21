"""
Faca um algoritmo que calcule o IMC de uma pessoa e mostre sua classificacao de
acordo com a tabela abaixo:

                | IMC         | Classificacao                |
                | < 18.5      | Abaixo do Peso               |
                | 18.6 - 24.9 | Saudavel                     |
                | 25.0 - 29.9 | Peso em excesso              |
                | 30.0 - 34.9 | Obesidade Grau I             |
                | 35.0 - 39.9 | Obesidade Grau II (severa)   |
                | >= 40.0     | Obesidade Grau III (morbida) |

"""
try:
    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    imc = peso / pow(altura, 2.0)

    if imc < 18.5:
        print('Abaixo do Peso')
    elif imc < 24.9:
        print('Saudavel')
    elif imc < 29.9:
        print('Peso em excesso')
    elif imc < 34.9:
        print('Obesidade Grau I')
    elif imc < 39.9:
        print('Obesidade Grau II (severa)')
    else:
        print('Obesidade Grau III (morbida)')

except ValueError:
    print('O formado do dado informado esta invalido!')
