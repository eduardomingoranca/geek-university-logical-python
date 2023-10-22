"""
Escreve um programa que verifique quais numeros entre 1000 e 9999 (inclusive) possuem
a propriedade seguinte: a soma dos dois digitos de mais baixa ordem com os dois digitos
de mais alta ordem elevada ao quadrado eh igual ao proprio numero. Por exemplo, para o
inteiro 3025, temos que:
30 + 25 = 55
55² = 3025
"""
contador = 1000
baixa_ordem = 0
alta_ordem = 0
while contador <= 9999:
    baixa_ordem = contador // 100
    alta_ordem = contador % 100
    soma_digitos = pow(baixa_ordem + alta_ordem, 2.0)

    if soma_digitos == contador:
        print(contador)
    contador = contador + 1
