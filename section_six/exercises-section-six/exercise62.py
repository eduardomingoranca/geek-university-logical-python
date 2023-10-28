"""
Se os numeros de 1 a 5 sao escritos em palavras: um, dois, tres, quatro, cinco, entao ha
2 + 4 + 4 + 6 + 5 = 21 letras usadas no total. Faca um programa que conte quantas letras
seriam utilizadas se todos os numeros de 1 a 1000 (mil) fossem escritos em palavras.
OBS: Nao conte espacos ou hifens.
"""
numero = 'um dois tres quatro cinco seis sete oito nove dez'

soma = 0
for n in numero.split(' '):
    soma = soma + len(n)

print(f'SOMA: {soma}')
