"""
Considerando a estrutura:

struct Vetor {
float x;
float y;
float z;
};

para representar um vetor no R³, implemente uma funcao que calcule a soma de dois
vetores. Essa funcao deve obedecer ao prototipo:

void soma (struct Vetor * v1, struct Vetor * v2, struct Vetor * res);

onde os parametros v1 e v2 sao ponteiros para os vetores a serem somadas, e o
parametro res eh um ponteiro para uma estrutura vetor onde o resultado da operacao
deve ser armazenado.
"""


def soma_vetor(a, b, a1, b2, r):
    z = 0
    while z < a:
        a1.append(float(input(f'V1[{z}]: ')))
        z = z + 1

    print()
    i = 0
    while i < b:
        b2.append(float(input(f'V2[{i}]: ')))
        i = i + 1

    for j in a1:
        r = r + j

    for k in b2:
        r = r + k

    return r


try:
    x = int(input('X: '))
    y = int(input('Y: '))

    v1 = []
    v2 = []
    res = 0

    print(f'RES: {soma_vetor(x, y, v1, v2, res)}')
except ValueError:
    print('FORMATO INVALIDO!')
