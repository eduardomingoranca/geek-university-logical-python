"""
Leia a nota e o numero de faltas de um aluno, e escreva seu conceito. De acordo com a
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma reducao de conceito.

    | NOTA         | CONCEITO (ATE 20 FALTAS) | CONCEITO (MAIS DE 20 FALTAS) |
    | 9.0 ate 10.0 |            A             |             B                |
    | 7.5 ate 8.9  |            B             |             C                |
    | 5.0 ate 7.4  |            C             |             D                |
    | 4.0 ate 4.9  |            D             |             E                |
    | 0.0 ate 3.9  |            E             |             E                |

"""
try:
    loop = True
    while loop:
        nota = float(input('Informe a nota do aluno: '))

        if 0.0 <= nota <= 10.0:
            faltas = int(input('Informe o numero de faltas do aluno: '))

            if 9.0 <= nota <= 10.0:

                if faltas <= 20:
                    print('A')
                else:
                    print('B')
            elif 7.5 <= nota <= 8.9:

                if faltas <= 20:
                    print('B')
                else:
                    print('C')
            elif 5.0 <= nota <= 7.4:
                if faltas <= 20:
                    print('C')
                else:
                    print('D')
            elif 4.0 <= nota <= 4.9:
                if faltas <= 20:
                    print('D')
                else:
                    print('E')
            elif 0.0 <= nota <= 3.9:
                print('E')
        else:
            loop = False
            print('NOTA INCORRETA!')

except ValueError:
    print('O valor informado esta invalido!')
