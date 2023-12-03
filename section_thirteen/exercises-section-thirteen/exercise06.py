"""
Faca um programa que receba do usuario um arquivo texto e mostre na tela quantas
vezes cada letra do alfabeto aparece dentro do arquivo.
"""

file = open('files/names.txt').read()

count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_e = 0
count_f = 0
count_g = 0
count_h = 0
count_i = 0
count_j = 0
count_k = 0
count_l = 0
count_m = 0
count_n = 0
count_o = 0
count_p = 0
count_q = 0
count_r = 0
count_s = 0
count_t = 0
count_u = 0
count_v = 0
count_w = 0
count_x = 0
count_y = 0
count_z = 0
for i in file:
    if i == 'a':
        count_a = count_a + 1
    elif i == 'b':
        count_b = count_b + 1
    elif i == 'c':
        count_c = count_c + 1
    elif i == 'd':
        count_d = count_d + 1
    elif i == 'e':
        count_e = count_e + 1
    elif i == 'f':
        count_f = count_f + 1
    elif i == 'g':
        count_g = count_g + 1
    elif i == 'h':
        count_h = count_h + 1
    elif i == 'i':
        count_i = count_i + 1
    elif i == 'j':
        count_j = count_j + 1
    elif i == 'k':
        count_k = count_k + 1
    elif i == 'l':
        count_l = count_l + 1
    elif i == 'm':
        count_m = count_m + 1
    elif i == 'n':
        count_n = count_n + 1
    elif i == 'o':
        count_o = count_o + 1
    elif i == 'p':
        count_p = count_p + 1
    elif i == 'q':
        count_q = count_q + 1
    elif i == 'r':
        count_r = count_r + 1
    elif i == 's':
        count_s = count_s + 1
    elif i == 't':
        count_t = count_t + 1
    elif i == 'u':
        count_u = count_u + 1
    elif i == 'v':
        count_v = count_v + 1
    elif i == 'w':
        count_w = count_w + 1
    elif i == 'x':
        count_x = count_x + 1
    elif i == 'y':
        count_y = count_y + 1
    elif i == 'z':
        count_z = count_z + 1

print(f'A letra A aparece {count_a} vez(es) no arquivo names.txt')
print(f'A letra B aparece {count_b} vez(es) no arquivo names.txt')
print(f'A letra C aparece {count_c} vez(es) no arquivo names.txt')
print(f'A letra D aparece {count_d} vez(es) no arquivo names.txt')
print(f'A letra E aparece {count_e} vez(es) no arquivo names.txt')
print(f'A letra F aparece {count_f} vez(es) no arquivo names.txt')
print(f'A letra G aparece {count_g} vez(es) no arquivo names.txt')
print(f'A letra H aparece {count_h} vez(es) no arquivo names.txt')
print(f'A letra I aparece {count_i} vez(es) no arquivo names.txt')
print(f'A letra J aparece {count_j} vez(es) no arquivo names.txt')
print(f'A letra K aparece {count_k} vez(es) no arquivo names.txt')
print(f'A letra L aparece {count_l} vez(es) no arquivo names.txt')
print(f'A letra M aparece {count_m} vez(es) no arquivo names.txt')
print(f'A letra N aparece {count_n} vez(es) no arquivo names.txt')
print(f'A letra O aparece {count_o} vez(es) no arquivo names.txt')
print(f'A letra P aparece {count_p} vez(es) no arquivo names.txt')
print(f'A letra Q aparece {count_q} vez(es) no arquivo names.txt')
print(f'A letra R aparece {count_r} vez(es) no arquivo names.txt')
print(f'A letra S aparece {count_s} vez(es) no arquivo names.txt')
print(f'A letra T aparece {count_t} vez(es) no arquivo names.txt')
print(f'A letra U aparece {count_u} vez(es) no arquivo names.txt')
print(f'A letra V aparece {count_v} vez(es) no arquivo names.txt')
print(f'A letra W aparece {count_w} vez(es) no arquivo names.txt')
print(f'A letra X aparece {count_x} vez(es) no arquivo names.txt')
print(f'A letra Y aparece {count_y} vez(es) no arquivo names.txt')
print(f'A letra Z aparece {count_z} vez(es) no arquivo names.txt')
