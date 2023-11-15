"""
Considerando a estrutura:
   struct Ponto {
       int x;
       int y;
   }
para representar um ponto em uma grade 2D, implemente uma funcao que indique se um
ponto p esta localizado dentro ou fora de um retangulo. O retangulo eh definido por seus
vertices inferior esquerdo v1 e superior direito v2. A funcao deve retornar 1 caso o ponto
esteja localizado dentro do retangulo e 0 caso contrario. Essa funcao deve obedecer ao
prototipo:
      int dentroRet (struct Ponto * v1, struct Ponto * v2, struct Ponto * p);
"""


def dentro_ret(param, param1, param2, param3, param4):
    a = ((param3 * param) * (param1 * param4)) / 2.0

    if a == param2:
        return 1

    return 0


try:
    x = float(input('X: '))
    y = float(input('Y: '))
    v1 = float(input('V1: '))
    v2 = float(input('V2: '))
    p = float(input('P: '))

    if dentro_ret(v1, v2, p, x, y) == 0:
        print('FORA DO RETANGULO')
    else:
        print('DENTRO DO RETANGULO')
except ValueError:
    print('FORMATO INVALIDO!')
