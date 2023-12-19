"""
Decoradores (Decorators)

O que sao decorators?

- Decorators sao funcoes;
- Decorators envolvem outras funcoes e aprimoram seus comportamentos;
- Decorators tambem sao exemplos de Higher Order Functions;
- Decorators tem uma sintaxe propria, usando "@" (Syntact Sugar / Acucar Sintatico)



|----------------------------------------|
|      Function Decorator                |
------------------------------------------


---------------------------------------------
| |---------------------------------------| |
| |        Funcao decorada                | |
| |---------------------------------------- |
| ------------------------------------------


# Decorators como funcoes (Sintaxe nao recomendada / Sem Acucar Sintatico)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce!')
        funcao()
        print('Tenha um otimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) a Geek University')


# Testando 1

# saudacao()


teste = seja_educado(saudacao)

teste()


# Testando 2


def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntax Sugar (Acucar Sintatico)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome eh Pedro')


# Testando

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()

"""
"""
|-------------------------------------------------------
|  Home    |  Servicos   | Produtos   | Administrativo |
--------------------------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/servicos

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/admin


# OBS: Nao eh codigo funcional (Que funcione) eh apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')


def home(request):
    return 'Pode acessar home'

@checa_login
def servicos(request):
    return 'Pode acessar servicos'


def produtos(request):
    return 'Pode acessar produtos'


@checa_login
def admin(request):
    return 'Pode acessar admin'

"""

# OBS: Nao confunda Decorator com Decorator Function
