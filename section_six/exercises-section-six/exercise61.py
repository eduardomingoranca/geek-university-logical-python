"""
Faca um programa que calcule o maior numero palindromo feito a partir do produto de
dois numeros de 3 digitos.
"""
i = 0
j = 0
palindromo = 0
while i <= 999:
    j = i
    while j <= 999:
        temp = str(i * j)
        tempInverso = temp[::-1]
        if temp == tempInverso:
            palindromoTemp = int(temp)
            if palindromoTemp > palindromo:
                palindromo = palindromoTemp
        j = j + 1
    i = i + 1

print(f'MAIOR PALINDROMO DE 3 DIGITOS: {palindromo}')
