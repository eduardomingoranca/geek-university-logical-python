"""
Estrutruas Logicas:
    - and (e), or (ou), not (não), is (eh)

Operadores unarios:
    - not;
Operadores binarios:
    - and, or, is;

Regras de funcionamento:
    - Para o 'and', ambos os valores precisam ser True
    - Para o 'or', um ou outro valor precisa ser True
    - Para o 'not', o valor do booleano eh invertido, ou seja, se for True, vira False, se for False vira True
    - Para o 'is', o valor eh comparado com um segundo.

"""
ativo = True
logado = False

if ativo:
    print('Bem-vindo usuario')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# ativo eh verdadeiro?
print(ativo is True)
