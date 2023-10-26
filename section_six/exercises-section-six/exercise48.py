"""
Faca um programa que some os termos de valor par da sequencia de Fibonacci, cujos
valores nao ultrapassem quatro milhoes.
"""
loop = False
anterior = 0
proximo = 1
while anterior < 4000000:
    print(f'{anterior}')
    fibonacci = anterior + proximo
    anterior = proximo
    proximo = fibonacci
