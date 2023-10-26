"""
Chico tem 1.50 metro e cresce 2 centimetros por ano, enquanto Ze tem 1.10 metros e
cresce 3 centimetros por ano. Escreva um programa que calcule e imprima quantos anos
serao necessarios para que Ze seja maior que Chico.
"""
chico = 1.50
ze = 1.10
anos = 0
while chico >= ze:
    chico = chico * 0.02
    ze = ze * 0.03
    anos = anos + 1

print(f'{anos} ANO(S)')
