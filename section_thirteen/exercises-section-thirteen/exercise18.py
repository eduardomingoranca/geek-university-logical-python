"""
Faca um programa que leia um arquivo contendo o nome e o preco de diversos produtos
(separados por linha), e calcule o total da compra.
"""

supermarket = open('files/supermarket.txt').read()

with open('files/total_price.txt', 'w') as file:
    file.write(supermarket)
    file.write('\n')

    i = 8
    total_price = 0
    while i < len(supermarket):
        total_price = total_price + float(supermarket[slice(i, i+5)])
        i = i + 14

    file.write('Total Price: $' + str(total_price))
