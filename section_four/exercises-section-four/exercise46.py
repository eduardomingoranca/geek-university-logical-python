"""
Faca um programa que leia um numero inteiro positivo de tres digitos (de 100 a 999).
Gere outro numero formado pelos digitos invertidos do numero lido. Exemplo:
    | Numero Lido = 123   |
    | Numero Gerado = 321 |
"""
inicio = 100
fim = 999
while inicio < fim:
    print(f'Numero lido = {inicio}')
    a = inicio // 100
    b = inicio % 100 // 10
    c = inicio % 100 % 10
    print(f'Numero gerado = {c}{b}{a}')
    inicio = inicio + 1
